"""Представление модуль отвечающего за акаунт пользователя и его командировки"""
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.middleware import csrf
from rest_framework.generics import CreateAPIView
from rest_framework import status
from railways_api.models import City
from .handler_business_trip import get_business_trip_information, insert_value_business_trip, \
    insert_value_hotel, insert_value_trip, get_body_request, serialize_hotel, serialize_trip, \
    serialize_business_trip
from .models import BusinessTrip, Trip, Hotel, UserTelegram, Cheque
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from .serializer import UserSerializer, LoginRequestSerializer, RegisterSerializer, CreateBusinessTripSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class LoginUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            authenticated_user = authenticate(**serializer.validated_data)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return Response({'status': 'Success'})
            else:
                return Response({'error': 'Invalid credentials'}, status=403)
        else:
            return Response(serializer.errors, status=400)


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def get_user(request: Request):
    return Response({'data': UserSerializer(request.user).data})


def register_telegram(request):
    """
    Регистрация через телеграм
    Args:
        request:

    Returns:

    """
    body = get_body_request(request)
    if request.method == 'POST':
        username = body['username']
        telegram_id = body['telegramId']
        first_name = body.get('firstName')
        last_name = body.get('lastName')
        user = User.objects.create_user(username, first_name=first_name, last_name=last_name)
        user.save()
        user_telegram = UserTelegram.objects.create(user=user, id_telegram=telegram_id)
        user_telegram.save()
        return HttpResponse(user)
    return HttpResponse(None)


def login_telegram(request):
    """
    Логинизация через телеграм
    Args:
        request:

    Returns:

    """
    id_telegram = request.POST['id_telegram']
    user_telegram = UserTelegram.objects.get(id_telegram=id_telegram)
    return HttpResponse(user_telegram.user)


def user_logout(request):
    """
    Выход пользователя из системы
    Args:
        request:

    Returns:

    """
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def get_business_trip(request: Request):
    """
    Метод возвращает краткую информацию о всех командировках пользователя
    Args:
        request:

    Returns:
    Json ответ со списком всех командировок пользователя и краткой информцией о них
    """
    id_user = request.user.id
    information = get_business_trip_information(id_user)
    return Response(information)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def update_business_trip(request: Request):
    """
    Обновление записи о командировке
    Args:
        request:

    Returns:

    """
    body = request.data
    id_b_t = int(body['idBT'])
    b_t = BusinessTrip.objects.get(pk=id_b_t)
    if request.user.id == b_t.user.pk:
        insert_value_business_trip(b_t, body)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def update_trip(request):
    """
    Обновление поездки
    Args:
        request:

    Returns:

    """
    body = request.data
    id_b_t = int(body['idBT'])
    b_t = BusinessTrip.objects.get(pk=id_b_t)
    if request.user.id == b_t.user.pk:
        is_first = int(body['isFirst'])
        trip = Trip.objects.filter(business_trip_id=id_b_t).get(is_first=is_first)
        insert_value_trip(trip, body)
        return HttpResponse('ok')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def update_hotel(request):
    """
    Обновление данных об отеле
    Args:
        request:

    Returns:

    """
    body = request.data
    id_b_t = int(body['idBT'])
    b_t = BusinessTrip.objects.get(pk=id_b_t)
    if request.user.id == b_t.user.pk:
        hotel = Hotel.objects.get(business_trip_id=id_b_t)
        insert_value_hotel(hotel, body)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def delete_business_trip(request):
    """
    Удаление записи о командировке
    Args:
        request:

    Returns:

    """
    body = get_body_request(request)
    b_t = BusinessTrip.objects.get(pk=int(body['idBT']))
    b_t.delete()
    return HttpResponse('ok')


class CreateBusinessTripView(CreateAPIView):
    queryset = BusinessTrip.objects.all()
    serializer_class = CreateBusinessTripSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        if request.user.id == int(request.data['user']):
            serializer = CreateBusinessTripSerializer(data=request.data)
            if serializer.is_valid():
                b_t = serializer.save()
                return Response(b_t.id)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response('Не верный пользователь', status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def create_trip(request):
    """
    Создание поездки
    Args:
        request:

    Returns:

    """
    body = request.data
    b_t = BusinessTrip.objects.get(pk=int(body['idBT']))
    if b_t.user.pk == request.user.id:
        trip = Trip.objects.create(
            business_trip_id=int(body['idBT']),
            transport=int(body['transport']),
            price_ticket=int(body['priceTicket']),
            is_first=int(body['isFirst']),
            transport_number=body['transportNumber'],
            date_departure=datetime.strptime(body['dateDeparture'], '%Y-%m-%d').date(),
            date_arrival=datetime.strptime(body['dateArrival'], '%Y-%m-%d').date(),
            city_from_id=City.objects.get(pk=int(body['cityFrom'])),
            city_to_id=City.objects.get(pk=int(body['cityTo'])),
            station_from=body['stationFrom'],
            station_to=body['stationTo']
        )
        trip.save()
        return Response(trip.pk)
    else:
        Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def create_hotel(request):
    """
    Создание отеля
    Args:
        request:

    Returns:

    """
    body = request.data
    b_t = BusinessTrip.objects.get(pk=int(body['idBT']))
    if b_t.user.pk == request.user.id:
        hotel = Hotel.objects.create(
            business_trip_id=int(body['idBT']),
            link=body['link'],
            name=body['name'],
            price=float(body['price']),
            date_check_in=datetime.strptime(body['checkIn'], '%Y-%m-%d').date(),
            date_check_out=datetime.strptime(body['checkOut'], '%Y-%m-%d').date()
        )
        hotel.save()
        return Response(hotel.pk)
    else:
        Response(status=status.HTTP_400_BAD_REQUEST)


def get_csrf(request):
    """
    Возвращает csrf токен
    Args:
        request:

    Returns:

    """
    return HttpResponse(csrf.get_token(request), content_type="text/plain")


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def get_full_info_business_trip(request):
    """
    Возвращает полную информацию о конкретной поездке
    Args:
        request:

    Returns:

    """
    id_b_t = request.GET['idBT']
    b_t = BusinessTrip.objects.get(pk=id_b_t)
    if request.user.id == b_t.user.pk:
        trips = Trip.objects.filter(business_trip_id=b_t.id)
        hotel = Hotel.objects.filter(business_trip_id=b_t.id)
        answer = {'businessTrip': serialize_business_trip(b_t),
                  'trip': [serialize_trip(trip) for trip in trips],
                  'hotel': serialize_hotel(hotel[0]) if len(hotel) > 0 else None}
        return Response(answer)
    else:
        return Response(status=400)
