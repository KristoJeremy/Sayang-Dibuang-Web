from django.shortcuts import render
from fitur_autentikasi.models import Profile, User
from django.shortcuts import render
from django.db.models import Sum

def leaderboard(request):
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
