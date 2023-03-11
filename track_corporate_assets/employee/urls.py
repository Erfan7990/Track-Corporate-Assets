from django.urls import path, include
from .views import *
urlpatterns = [
    path("", Employees_Comment.as_view(), name="employee"),
    path("sslc/status/", sslc_status, name="status"),
    path("sslc/complete/<val_id>/<tran_id>", sslc_complete, name="ssl_complete"),
]