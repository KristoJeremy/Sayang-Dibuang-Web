from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
    form = CreateReview(request.POST)

    if request.method == "POST":
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = Profile.objects.get(user=request.user)
            new_review.save()
            return redirect('information:all_review')

    context = {
        "form": form
        }
    return render(request, "information/createreview.html", context)

def all_review(request):
    return render(request, 'information/lihatreview.html')

@login_required(login_url='/login/')
def review_detail(request,id):
    # review = Review.objects.select_related('profile').select_related('user').get(id=id)
    user = request.user 

    context = {
        # 'review':review,
        'user':user
    }
    return render(request, 'information/review-detail.html')

@login_required(login_url='/login/')
def delete_review(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect("information/lihatreview.html")
