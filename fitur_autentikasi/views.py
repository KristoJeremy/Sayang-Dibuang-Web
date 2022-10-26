from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from fitur_autentikasi.forms import ProfileForm, UserForm

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