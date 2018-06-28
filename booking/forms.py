from django import forms

from .models import *
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['title', 'booking_date', 'booking_slot']
        widgets = {
            'booking_date': DateInput()
        }