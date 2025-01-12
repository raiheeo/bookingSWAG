from .serializers import (HotelListSerializer, HotelImageSerializer, RoomListSerializer, RoomImageSerializer, CityListSerializer,
BookingSerializer, RatingSerializer, ReviewSerializer, UserSerializer, CityDetailSerializer, HotelDetailSerializer, RoomDetailSerializer)

from django.shortcuts import render
from .models import Hotel, HotelImage, Room, RoomImage, City, Booking, Rating, Review, User
from rest_framework import viewsets, generics


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset =  Review.objects.all()
    serializer_class = ReviewSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset =  Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer