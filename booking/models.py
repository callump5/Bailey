# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Booking(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __unicode__(self):
        return self.title

