from django.shortcuts import render
from fitur_autentikasi.models import Profile, User
from leaderboard.models import Message
from django.shortcuts import render
from django.db.models import Sum
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from random import choice


def leaderboard(request):
    return render(request, 'leaderboard.html')

def show_json(request):
    num_of_user = Profile.objects.count()
    data = []
    counter = 1

    if num_of_user < 10:
        temp = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')
    else:
        temp = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')[:10]

    for item in temp:
        if counter == 1:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 'Gold'})
            counter += 1
        elif counter == 2:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 'Silver'})
            counter += 1
        elif counter == 3:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 'Bronze'})
            counter += 1
        else:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 'Standard'})
            counter += 1

    return JsonResponse(data, safe=False)

def add_message (request):
    if request.method == 'POST':
        random_message = request.POST.get("random_message")

        new_message = Message(random_message=random_message)
        new_message.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponse(b"CREATED", status=201)

def show_message_json (request):
        pks = Message.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        selected_message = Message.objects.get(pk=random_pk)
        context = {
            "data" : selected_message
        }
        data_message = [{'message' : selected_message.random_message}]
        return JsonResponse(data_message, safe=False)