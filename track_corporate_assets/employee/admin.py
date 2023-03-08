from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'name', 'email', 'address']
    
@admin.register(Device_Return)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name','device_name']
