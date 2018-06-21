# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from djreservation.views import ProductReservationView
from .models import *

class MyObjectReservation(ProductReservationView):
        base_model = Booking     # required
        amount_field = 1