from django.contrib import admin
from .models import Hotel, HotelImage, Room, RoomImage, City, Booking, Rating, Review, User
from modeltranslation.admin import TranslationAdmin


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1


class RoomInline(admin.TabularInline):
    model = Room
    extra = 1
    show_change_link = True  #I've found  here - https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#inlines


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInline, RoomInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(HotelImage)
admin.site.register(RoomImage)
admin.site.register(City)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Booking)
