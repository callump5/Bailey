# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class ServiceInfo(models.Model):

    description = HTMLField()

    def __unicode__(self):
        return 'Service Info'

class Service(models.Model):

    service = models.CharField(max_length=200)

    def __unicode__(self):
       return self.service


class RepairInfo(models.Model):

    description = HTMLField()

    def __unicode__(self):
        return 'RepairInfo'

class Repairs(models.Model):

    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title