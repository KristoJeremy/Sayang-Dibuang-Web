from django.shortcuts import render
from fitur_autentikasi.models import Profile
from django.shortcuts import render
from django.db.models import Sum

def leaderboard(request):
    user_leaderboard = User.objects.alias(
        total_points=Sum('Profile__poin')
    ).order_by('-total_points')[:10]

    return render(request, 'leaderboard.html', {'user_leaderboard':user_leaderboard})
