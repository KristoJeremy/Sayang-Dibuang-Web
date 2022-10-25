import profile
from django.urls import path
from fitur_autentikasi.views import *

app_name = 'fitur_autentikasi'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<str:username>', show_profile, name='show_profile'),
    path('user-data/<str:username>', get_user_data, name='get_user_data'),
]