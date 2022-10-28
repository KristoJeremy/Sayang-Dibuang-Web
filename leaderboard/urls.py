from django.urls import path
from leaderboard.views import leaderboard, show_json

app_name = 'leaderboard'

urlpatterns = [
    path('', leaderboard, name='leaderboard'), 
    path('json/', show_json, name='show_json')
]