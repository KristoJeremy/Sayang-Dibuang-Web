from django.urls import path
from leaderboard.views import leaderboard, show_json, add_message, show_message_json

app_name = 'leaderboard'

urlpatterns = [
    path('', leaderboard, name='leaderboard'), 
    path('json/', show_json, name='show_json'),
    path('json-message/', show_message_json, name='show_message_json'),
    path('send-message/', add_message, name='add_message' )
]