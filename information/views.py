from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse

from information.forms import *
from information.models import *
from fitur_autentikasi.models import Profile

def index(request):
    user = request.user
    if not request.user.is_authenticated:
        user = None
    context = {
        'user': user,
    }
    return render(request, 'information/index/index.html', context)

@login_required(login_url='/login/')
def create_review(request):

    if request.method == "POST":
        form = CreateReview(request.POST)
        if form.is_valid():
            x = Profile.objects.get(user=request.user)
            if (x != None):
                new_review = form.save(commit=False)
                new_review.user = x
                new_review.save()
                return redirect('information:all_review')
            
    form = CreateReview()
    context = {"form": form}
    return render(request, "information/createreview.html", context)

def all_review(request):
    return render(request, 'information/lihatreview.html')

def all_review_json(request):
    list = Review.objects.all().order_by('-created')
    data = []

    for i in list:
        # print(i.user)
        username = i.user.user.username
        data.append({
            'username': username, 'judul': i.judul,
            'deskripsi': i.deskripsi, 'created': i.created, 'pk': i.pk
            })
    # print(data)
    return JsonResponse(data, safe=False)

@login_required(login_url='/login/')
def review_detail(request,id):
    review = Review.objects.select_related('user').get(id=id)
    user = request.user 

    context = {
        'review':review,
        'user':user
    }
    return render(request, 'information/review-detail.html', context)

@login_required(login_url='/login/')
def delete_review(request, id):
    review = Review.objects.get(user=Profile.objects.get(user=request.user), id=id)
    review.delete()
    return redirect("information:all_review")
