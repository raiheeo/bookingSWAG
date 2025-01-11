from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KZ')
    age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(18), MaxValueValidator(75)], null=True, blank=False)
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('owner', 'Owner'),
        ('admin', 'Admin'),
    )
    status = models.CharField(max_length=32, choices=ROLE_CHOICES, default='client')
    registered_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class City(models.Model):
    city_name = models.CharField(max_length=64, unique=True)
    city_image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return f'{self.city_name}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.CharField(max_length=64)
    hotel_stars = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)])
    location = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.hotel_name


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image/')

    def __str__(self):
        return str(self.hotel_image)


class Room(models.Model):
    room_number = models.SmallIntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('luxury', 'Luxury'),
        ('family', 'Family'),
        ('single', 'Single'),
        ('double', 'Double'),
    )
    room_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    STATUS_CHOICES = (
        ('free', 'Free'),
        ('ordered', 'Ordered'),
        ('busy', 'Busy'),
    )
    room_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='free')
    all_inclusive = models.BooleanField(default=False, verbose_name='Bonus')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_description = models.TextField()
    room_video = models.FileField(upload_to='room_videos/')

    def __str__(self):
        return f'{self.hotel}, {self.room_number}'

    class Meta:
        unique_together = ('hotel', 'room_number')


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f'{self.room}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    created_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}, {self.stars}'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    BOOK_STATUS_CHOICES = (
        ('cancelled', 'Cancelled'),
        ('confirmed', 'Confirmed')
    )
    book_status = models.CharField(max_length=32)

    def __str__(self):
       return f'{self.room}, {self.check_in}, {self.check_out}'


