from django.urls import path
from fitur_autentikasi.views import *

app_name = 'fitur_autentikasi'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]