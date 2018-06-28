# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import timedelta
# Create your models here.

class Booking(models.Model):


    SLOTS = [(i, i) for i in range(9, 18)]
    title = models.CharField(max_length=200)
    booking_date = models.DateField()
    booking_slot = models.IntegerField(max_length=30, choices=SLOTS)
    def __unicode__(self):
        return self.title

