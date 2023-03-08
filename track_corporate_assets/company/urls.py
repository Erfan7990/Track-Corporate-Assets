from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Index, name="index"),
    path('signin/', signin, name="signin"),
    path('signup/', SignUp, name="signup"),
    path('logout/', logout_page, name="logout"),
    path("add-employee/", Add_Employee, name="add_employee"),
    path("add-device/", add_devices, name="add_devices")
]