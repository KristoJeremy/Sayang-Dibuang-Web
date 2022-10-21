from django.shortcuts import render
from django.http import HttpResponse
from fitur_autentikasi.models import Profile

# Create your views here.
def hello_world(request):

    user = Profile.objects.get(user=request.user)
    print(request.user.first_name)
    print(user.get_fullname())

    return HttpResponse(user.get_fullname())
