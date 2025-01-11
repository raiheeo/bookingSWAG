from .models import Hotel, City, Room
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description', 'location', 'country')


@register(City)
class ProductTranslationOptions(TranslationOptions):
    fields = ('city_name', )

@register(Room)
class ProductTranslationOptions(TranslationOptions):
    fields = ('room_description', )