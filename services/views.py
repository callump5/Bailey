# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import ServiceInfo, Service, RepairInfo, Repairs
# Create your views here.

def get_services(request):

    info = ServiceInfo.objects.all()
    services = Service.objects.all()

    return render(request, 'services/services.html', {'info':info,
                                                      'services': services})

def get_repairs(request):
    info = RepairInfo.objects.all()
    repairs = Repairs.objects.all()

    return render(request, 'services/repairs.html', {'info': info,
                                                     'repairs': repairs})

