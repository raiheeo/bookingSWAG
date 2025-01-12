from rest_framework.routers import DefaultRouter, SimpleRouter
from django.contrib import admin
from django.urls import path, include
from .views import HotelListAPIView, RoomDetailAPIView, RoomListAPIView,ReviewViewSet, RatingViewSet, CityListAPIView, BookingViewSet, \
    UserViewSet, HotelListAPIView, CityListAPIView, CityDetailAPIView, HotelDetailAPIView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users_list')
router.register(r'review', ReviewViewSet, basename='review_list')



urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room_detail'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail')
]