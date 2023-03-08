from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from django.utils.text import slugify


class Device(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField( null=True, blank=True)
    device_image = models.ImageField(upload_to='device')
    
    
    
    def __str__(self):
        return self.name


