# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import HomeContent

# Create your views here.


def get_home(request):
    info = HomeContent.objects.all()
    return render(request, 'home/home.html', {'info': info})