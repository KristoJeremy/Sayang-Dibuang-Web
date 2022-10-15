from django.shortcuts import render
from .models import Crowdfund

# Create your views here.
def show_crowdfundings(request):
    crowdfunds = Crowdfund.objects.all()
    context = {"crowdfunds": crowdfunds}
    return render(request, "crowdfunding.html", context)
