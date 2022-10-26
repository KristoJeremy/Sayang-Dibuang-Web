from django.urls import path
from leaderboard.views import leaderboard

app_name = 'leaderboard'

urlpatterns = [
    path('', leaderboard, name='leaderboard'), 
]