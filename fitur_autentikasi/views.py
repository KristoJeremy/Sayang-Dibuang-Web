from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core import serializers

from fitur_autentikasi.forms import *
from fitur_autentikasi.models import Profile

from django.views.decorators.csrf import csrf_exempt
import json, re

# Create your views here.
def register(request):
    form = UserForm()
    profile_form = ProfileForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid() :
            new_user = form.save()
            profile_form = ProfileForm(request.POST, instance=new_user.profile)
            profile_form.save()

            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('fitur_autentikasi:login')
    
    context = {'form':form, 'profile_form': profile_form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('information:index_information')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('information:index_information')

@login_required(login_url='/login/')
def show_profile(request, username):
    user = request.user
    user_update_form = UserUpdateForm()
    profile_form = ProfileForm()

    # User hanya dapat mengakses halaman profil user itu sendiri
    if user.username == username:
        context = {'user': user, 'user_update_form': user_update_form,'profile_form': profile_form}
        return render(request, 'profile.html', context)
    else:
        return HttpResponseNotFound()

@login_required(login_url='/login/')
def get_user_data(request, username):
    user = request.user

    if request.method == "GET" and user.username == username:

        # Mendapatkan objek dari database
        profile_data = Profile.objects.filter(user = user)
        profile_data_json = serializers.serialize('json', profile_data)
        profile_data_json = re.sub('"user": .*,', f'"user": {getJsonUser(user)} ,', profile_data_json)

        return HttpResponse(profile_data_json, content_type="application/json")

    return HttpResponseNotFound()

def getJsonUser(user):
    user_data = {}

    user_data['id'] = user.pk
    user_data['is_superuser'] = user.is_superuser
    user_data['username'] = user.username
    user_data['first_name'] = user.first_name
    user_data['last_name'] = user.last_name
    user_data['email'] = user.email

    return json.dumps(user_data)

@login_required(login_url='/login/')
def update_user_data(request, username):
    user = request.user

    if request.method == "POST" and user.username == username:
        user_update_form = UserUpdateForm(request.POST, instance=user)

        if user_update_form.is_valid():
            user_update_form.save()

        profile_form = ProfileForm(UPOST(request.POST,user.profile), instance=user.profile)

        if profile_form.is_valid():
            profile_form.save()
        else:
            errors = profile_form.errors.as_json()
            return JsonResponse(errors, safe=False, status=400)
        
        return HttpResponse("OK")

    return HttpResponseNotFound()

# Source: https://stackoverflow.com/questions/8216353/django-update-one-field-using-modelform
# by: Roman Semko
from django.forms.models import model_to_dict
from copy import copy

def UPOST(post, obj):
    '''Updates request's POST dictionary with values from object, for update purposes'''
    post = copy(post)
    for k,v in model_to_dict(obj).items():
        if k not in post: 
            post[k] = v
    return post

# For pbp_django_auth
# https://pub.dev/packages/pbp_django_auth
@csrf_exempt
def login_ajax(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)