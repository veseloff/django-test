from rest_framework.serializers import Serializer, ModelSerializer, CharField
from django.contrib.auth.models import User
from user_profile.models import BusinessTrip, Trip, Hotel
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

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            first_name=self.validated_data['firstname'],
            last_name=self.validated_data['last_name']
        )
        user.save()
        return user


class CreateBusinessTripSerializer(ModelSerializer):
    fromCity = CharField(source='businesstrip_from_city')
    toCity = CharField(source='businesstrip_to_city')
    budget = serializers.IntegerField(source='businesstrip_credit')
    begin = serializers.DateField(source='businesstrip_date_finish')
    end = serializers.DateField(source='businesstrip_date_finish')

    class Meta:
        model = BusinessTrip
        fields = ['name', 'user', 'fromCity', 'toCity', 'budget', 'begin', 'end', 'status']

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


# class CreateTripSerializer(ModelSerializer):
#     is_first = serializers.IntegerField(source='trip_is_first')
#     business_trip = serializers.(source='trip_business_trip')
#     price_ticket = serializers.IntegerField(source='trip_price_ticket')
#     begin = serializers.DateField(source='businesstrip_date_finish')
#     end = serializers.DateField(source='businesstrip_date_finish')
#
#     class Meta:
#         model = Trip
#         fields = ['name', 'user', 'cityFrom', 'cityTo', 'budget', 'begin', 'end', 'status']
#
#     def save(self, *args, **kwargs):
#         b_t = BusinessTrip.objects.create(
#             user=self.validated_data['user'],
#             name=self.validated_data['name'],
#             from_city=self.validated_data['businesstrip_from_city'],
#             to_city=self.validated_data['businesstrip_to_city'],
#             credit=self.validated_data.get('businesstrip_credit'),
#             date_start=datetime.strptime(self.data['begin'], '%Y-%m-%d').date(),
#             date_finish=datetime.strptime(self.data['end'], '%Y-%m-%d').date(),
#             status=self.validated_data['status']
#         )
#         b_t.save()
#         return b_t
