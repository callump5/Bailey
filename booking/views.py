# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Booking
from .forms import *
from django.contrib import messages
# Create your views here.


def booking_list(request):
    bookings = Booking.objects.all()

    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():

            date = form.cleaned_data.get('booking_date')
            slot = form.cleaned_data.get('booking_slot')
            if Booking.objects.filter(booking_date=date, booking_slot=slot):
                messages.warning(request, 'That time slot is unavailable!')
                form = BookingForm

            else:
                form.save()
                messages.success(request, 'You succesfully requested a quote for ' + str(date) + ' ' + str(slot)+ ':00')

                return redirect('bookings')
    else:
        form = BookingForm
    return render(request, 'booking/form.html', {'form': form})
