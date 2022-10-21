from django.shortcuts import render
from .models import Crowdfund
from .forms import CrowdfundForm


def show_crowdfundings(request):
    crowdfunds = Crowdfund.objects.all()
    context = {"crowdfunds": crowdfunds}
    return render(request, "crowdfundings.html", context)


def show_crowdfunding_by_id(request, id):
    crowdfund = Crowdfund.objects.get(pk=id)
    context = {"crowdfund": crowdfund}
    return render(request, "crowdfunding.html", context)


def create_crowdfund(request):
    form = CrowdfundForm()

    if request.method == "POST":
        pass

    context = {"form": form}
    return render(request, "create_crowdfund.html", context)


# def show_crowdfundings_json(request):
#     crowdfunds = Crowdfund.objects.all()
#     return HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")
