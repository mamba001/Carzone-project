from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50px" />'.format(object.car_photo.url))

    thumbnail.short_description = 'car image'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('thumbnail', 'car_title', 'id')
    list_editable = ('is_featured',)

    search_fields = ('model', 'year', 'car_title', 'id', 'body_style', 'fuel_type')
    list_filter = ('model', 'city', 'body_style', 'year')


admin.site.register(Car, CarAdmin)
