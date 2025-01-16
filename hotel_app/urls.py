from rest_framework.routers import DefaultRouter, SimpleRouter
from django.contrib import admin
from django.urls import path, include
from .views import (HotelListAPIView, RoomDetailAPIView, RoomListAPIView, RatingCreateAPIView,  ReviewCreateAPIView, CityListAPIView, \
    BookingViewSet, \
    UserViewSet, HotelListAPIView, CityListAPIView, CityDetailAPIView, HotelDetailAPIView, HotelCreateAPIView, \
    HotelOwnerListAPIView, HotelOwnerEditAPIView,
    ReviewEditCreateAPIView, RatingEditCreateAPIView, RoomCreateAPIView, RoomOwnerEditAPIView, RoomOwnerListAPIView)
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users_list')


urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('hotel/create/', HotelCreateAPIView.as_view(), name='hotel_create'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('rooms/create/', RoomCreateAPIView.as_view(), name='room_create'),
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('rooms_list/', RoomOwnerListAPIView.as_view(), name='rooms_owner_list'),
    path('rooms_list/<int:pk>/', RoomOwnerEditAPIView.as_view(), name='rooms_owner_edit_list'),
    path('hotel_list/', HotelOwnerListAPIView.as_view(), name='hotel_owner_list'),
    path('hotel_list/<int:pk>/', HotelOwnerEditAPIView.as_view(), name='hotel_owner_edit_list'),
    path('review/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewEditCreateAPIView.as_view(), name='review_edit'),
    path('rating/', RatingCreateAPIView.as_view(), name='rating_create'),
    path('rating/<int:pk>/', RatingEditCreateAPIView.as_view(), name='rating_edit'),
]