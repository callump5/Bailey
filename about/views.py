# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import AboutInfo
# Create your views here.

def get_about(request):
    info = AboutInfo.objects.all()
    return render(request, 'about/about.html', {'info': info})