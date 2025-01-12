from .models import Hotel, HotelImage, Room, RoomImage, City, Booking, Rating, Review, User
from rest_framework import serializers


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


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'hotel_image']


class CityDetailSerializer(serializers.ModelSerializer):
    city_hotels = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image', 'city_hotels']



class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    owner = UserSimpleSerializer
    hotel_rooms = RoomListSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'hotel_image',
        'country', 'hotel_stars', 'description', 'location', 'owner', 'hotel_rooms']
