from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User

# Model Import
from company.models import *
# Create your models here.


class Employee(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    device = models.ManyToManyField(Device)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    given_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    


class Device_Return(BaseModel):
    employee_name = models.CharField(max_length=100, null=True, blank=True)
    device_name = models.ForeignKey(Device, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True, blank=True)
    
    
    def __str__(self):
        return self.employee_name