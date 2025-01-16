from django_filters import FilterSet, NumberFilter
from .models import *


class HotelFilter(FilterSet):
    hotel_stars_min = NumberFilter(field_name='hotel_stars', lookup_expr='gte', label='Min stars')
    hotel_stars_max = NumberFilter(field_name='hotel_stars', lookup_expr='lte', label='Max stars')

    class Meta:
        model = Hotel
        fields = ['hotel_stars']

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'all_inclusive': ['exact'],
            'price': ['gt', 'lt'],
        }

class BookingFilter(FilterSet):
    class Meta:
        model = Booking
        fields = {
            'check_in': ['exact'],
            'check_out': ['exact']
        }
