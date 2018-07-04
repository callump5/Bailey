from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^bookings/$', booking_list, name='booking'),
    url(r'^bookings/create/$', create_booking)
]