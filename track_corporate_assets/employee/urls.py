from django.urls import path, include
from .views import *
urlpatterns = [
    path("", Employee_DeviceReturn, name="employee")
]