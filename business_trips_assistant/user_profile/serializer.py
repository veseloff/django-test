from rest_framework.serializers import Serializer, ModelSerializer, CharField
from django.contrib.auth.models import User
from user_profile.models import BusinessTrip, UserTelegram
from rest_framework import serializers
from datetime import datetime


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class LoginRequestSerializer(Serializer):
    model = User

    username = CharField(required=True)
    password = CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterSerializer(ModelSerializer):
    firstname = serializers.CharField(source='user_first_name')
    lastname = serializers.CharField(source='user_last_name')

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'firstname', 'lastname']

    def save(self, *args, **kwargs):
        user = User.objects.create_user(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            first_name=self.validated_data['user_first_name'],
            last_name=self.validated_data['user_last_name']
        )
        user.save()
        return user


class CreateBusinessTripSerializer(ModelSerializer):
    fromCity = CharField(source='businesstrip_from_city')
    toCity = CharField(source='businesstrip_to_city')
    budget = serializers.IntegerField(source='businesstrip_credit')
    begin = serializers.DateField(source='businesstrip_date_start')
    end = serializers.DateField(source='businesstrip_date_finish')

    class Meta:
        model = BusinessTrip
        fields = ['name', 'user', 'fromCity', 'toCity', 'budget', 'begin', 'end', 'status']

    def is_valid_date(self):
        start = datetime.strptime(self.data['begin'], '%Y-%m-%d').date(),
        finish = datetime.strptime(self.data['end'], '%Y-%m-%d').date(),
        return start < finish

    def save(self, *args, **kwargs):
        b_t = BusinessTrip.objects.create(
            user=self.validated_data['user'],
            name=self.validated_data['name'],
            from_city=self.validated_data['businesstrip_from_city'],
            to_city=self.validated_data['businesstrip_to_city'],
            credit=self.validated_data.get('businesstrip_credit'),
            date_start=datetime.strptime(self.data['begin'], '%Y-%m-%d').date(),
            date_finish=datetime.strptime(self.data['end'], '%Y-%m-%d').date(),
            status=self.validated_data['status']
        )
        b_t.save()
        return b_t


class UserTelegramSerializer(ModelSerializer):
    idTelegram = serializers.IntegerField(source='id_telegram')

    class Meta:
        model = UserTelegram
        fields = ['user', 'idTelegram']