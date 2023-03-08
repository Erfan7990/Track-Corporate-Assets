from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'device_image']