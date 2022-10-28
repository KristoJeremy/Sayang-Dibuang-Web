from unicodedata import name
from django.urls import path
from information.views import *

app_name = 'information'

urlpatterns = [
    path('', index, name='index_information'),
    path('review/', all_review, name='all_review'),
    path('create/', create_review, name='create_review'),
    path('delete/<int:id>', delete_review, name='delete_review'),
    path('<int:id>/', review_detail, name='review_detail')
]