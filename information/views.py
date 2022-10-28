from multiprocessing import context
from django.shortcuts import render, redirect

def index(request):
    user = request.user
    if not request.user.is_authenticated:
        user = None
    context = {
        'user': user
    }
    return render(request, 'information/index/index.html', context)
