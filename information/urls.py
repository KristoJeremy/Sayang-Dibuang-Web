from django.urls import path
from .views import *

app_name = 'information'

urlpatterns = [
    path('', index, name='index_information'),
]