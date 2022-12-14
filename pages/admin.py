from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50px" />'.format(object.photo.url))

    thumbnail.short_description = 'image'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('thumbnail', 'first_name', 'id')
    search_fields = ('first_name', 'last_name', 'designation', 'id')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)



"""
user: myadmin
password: ddS45-123
"""
