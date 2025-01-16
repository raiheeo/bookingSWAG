from .models import Hotel, HotelImage, Room, RoomImage, City, Booking, Rating, Review, User
from rest_framework import serializers
import datetime
from django.utils import timezone


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image', ]


class RoomListSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'room_status', 'price', 'all_inclusive', 'room_image']

class RoomDetailSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'price', 'all_inclusive', 'room_image', 'room_video', 'room_description']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image', ]


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image']


class CitySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name', ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class RatingDetailSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer()
    created_Date = serializers.SerializerMethodField()
    hotel = serializers.CharField(source='hotel.hotel_name')

    class Meta:
        model = Rating
        fields = ['id', 'user', 'stars', 'created_Date', 'hotel']


    def get_created_Date(self, obj):
        created_date = obj.created_Date
        if isinstance(created_date, datetime.datetime):
            created_date = created_date.date()
        return created_date.strftime('%d-%m-%Y') if created_date else None


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer()
    created_date = serializers.SerializerMethodField()
    hotel = serializers.CharField(source='hotel.hotel_name')

    class Meta:
        model = Review
        fields = ['user', 'text', 'created_date', 'hotel']

    def get_created_date(self, obj):
        created_date = obj.created_date
        if isinstance(created_date, datetime.datetime):
            created_date = created_date.date()
        return created_date.strftime('%d-%m-%Y') if created_date else None

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'hotel_image', 'country']


class CityDetailSerializer(serializers.ModelSerializer):
    city_hotels = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image', 'city_hotels']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    owner = UserSimpleSerializer()
    hotel_rooms = RoomDetailSerializer(many=True, read_only=True)
    reviews = ReviewDetailSerializer(many=True, read_only=True)
    hotel_reviews = ReviewDetailSerializer(many=True)
    hotel_ratings = RatingDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = [
            'id',
            'hotel_name',
            'owner',
            'city',
            'hotel_image',
            'country',
            'hotel_stars',
            'description',
            'location',
            'hotel_rooms',
            'hotel_reviews',
            'reviews',
            'hotel_ratings',
        ]


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
