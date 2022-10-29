from django.shortcuts import render
from fitur_autentikasi.models import Profile, User
from django.shortcuts import render
from django.db.models import Sum
from django.core import serializers
from django.http import HttpResponse, JsonResponse

def leaderboard(request):
    """
    num_of_user = Profile.objects.count()

    if num_of_user == 0:
        user_leaderboard = 'The leaderboard is empty'
    elif num_of_user < 10:
        user_leaderboard = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')
    else:
        user_leaderboard = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')[:10]

    return render(request, 'leaderboard.html', {'user_leaderboard':user_leaderboard})
    """
    return render(request, 'leaderboard.html')

def show_json(request):
    num_of_user = Profile.objects.count()
    data = []

    if num_of_user < 10:
        temp = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')
    else:
        temp = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')[:10]

    for item in temp:
        data.append({'username' : item.user.username, 'poin' : item.poin})
    
    return JsonResponse(data, safe=False)