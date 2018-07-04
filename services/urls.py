from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^services/', get_services),
    url(r'^maintenance/', get_repairs),
]