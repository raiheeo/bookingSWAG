from .serializers import (HotelListSerializer, HotelImageSerializer, RoomListSerializer, RoomImageSerializer, CityListSerializer,
BookingSerializer, RatingDetailSerializer, ReviewDetailSerializer, UserSerializer,
                          CityDetailSerializer, HotelDetailSerializer, RoomDetailSerializer,
                          HotelSerializer, RatingSerializer, ReviewSerializer, RoomSerializer)

from django.shortcuts import render
from .models import Hotel, HotelImage, Room, RoomImage, City, Booking, Rating, Review, User
from rest_framework import viewsets, generics
from .permissions import CheckOwner, CheckOwnerEdit, CheckAuthor
from .filters import HotelFilter, RoomFilter, BookingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name', 'country']


class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['city_name']


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = RoomFilter
    search_fields = ['room_type']

class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset =  Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CheckAuthor]


class ReviewEditCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [CheckAuthor]

    def get_queryset(self):
        return Review.objects.all.filter(user=self.request.user)

class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [CheckAuthor]

class RatingEditCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [CheckAuthor]

    def get_queryset(self):
        return Rating.objects.all.filter(user=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    queryset =  Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookingFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
         return User.objects.filter(id=self.request.user.id)

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class HotelCreateAPIView(generics.CreateAPIView):
    serializer_class = HotelSerializer
    permission_classes = [CheckOwner]

class HotelOwnerListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    permission_classes = [CheckOwner]

    def get_queryset(self):
        return Hotel.objects.filter(owner=self.request.user)

class HotelOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [CheckOwner, CheckOwnerEdit]


class RoomCreateAPIView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    permission_classes = [CheckOwner, CheckOwnerEdit]

class RoomOwnerListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    permission_classes = [CheckOwner]

    def get_queryset(self):
        user_instance = self.request.user
        return Room.objects.filter(hotel__owner=user_instance)

class RoomOwnerEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [CheckOwner, CheckOwnerEdit]






