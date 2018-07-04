# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Booking
from .forms import *
from django.contrib import messages
from django.views.decorators import csrf
# Create your views here.


def booking_list(request):
    bookings = Booking.objects.all()

    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():

            booking = booking_form.save(False)
            booking.save()

            messages.success(request, 'You successfully made a booking!')

            return redirect('booking')
        else:
            dates = [(i) for i in range(9, 18)]
            objs = Booking.objects.filter(booking_date=booking_form.cleaned_data['booking_date'])

            for ob in objs:
                if ob.booking_time in dates:
                    dates.remove(ob.booking_time)

            message = 'Booking time already exists - available times: '

            for ob in dates:
                message += str(ob) + ':00, '
            messages.error(request, message)
    else:
        booking_form = BookingForm()
    return render(request, 'booking/form.html', {'booking_form': booking_form})
