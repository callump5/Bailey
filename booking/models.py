# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import timedelta
from tinymce.models import HTMLField
# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    description = models.TextField()
    booking_date = models.DateField()
    SLOTS = [(i, i) for i in range(9, 18)]
    booking_time = models.IntegerField(choices=SLOTS)

    class Meta:
        unique_together = ('booking_date', 'booking_time')

    def __unicode__(self):
        return self.name




