from django.contrib import admin
from .models import *
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = [ 'event_name', 'data', 'date_time', 'location', 'image', 'is_liked']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['like_id', 'user', 'liked_id']

admin.site.register(Event,EventAdmin)
admin.site.register(Like,LikeAdmin)