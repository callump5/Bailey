# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class HomeContent(models.Model):

    description = HTMLField()

    def __unicode__(self):
        return 'Home Info'