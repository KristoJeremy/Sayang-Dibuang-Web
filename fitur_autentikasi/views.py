from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.core import serializers

from fitur_autentikasi.forms import ProfileForm, UserForm
from fitur_autentikasi.models import Profile

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
            return redirect('test_app:hello_world')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('fitur_autentikasi:login')

@login_required(login_url='/login/')
def show_profile(request, username):
    user = request.user

    # User hanya dapat mengakses halaman profil user itu sendiri
    if user.username == username:
        context = {'user': user}
        return render(request, 'profile.html', context)
    else:
        return HttpResponseNotFound()

def get_user_data(request, username):
    user = request.user
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    print(request.headers)

    if request.method == "GET" and user.username == username:

        # Mendapatkan objek dari database
        profile_data = Profile.objects.filter(user = user)
        profile_data_json = serializers.serialize('json', profile_data)

        return HttpResponse(profile_data_json, content_type="text/json")

    return HttpResponseNotFound()