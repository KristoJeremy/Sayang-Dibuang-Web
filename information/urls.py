from unicodedata import name
from django.urls import path
from information.views import *

app_name = 'information'

urlpatterns = [
    path('', index, name='index_information'),
    path('review/', all_review, name='all_review'),
    path('review/all/', all_review_json, name="all_review_json"),
    path('review/create/', create_review, name='create_review'),
    path('review/<int:id>/delete', delete_review, name='delete_review'),
    path('review/<int:id>/', review_detail, name='review_detail')
]