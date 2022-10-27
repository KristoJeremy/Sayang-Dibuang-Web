from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Crowdfund
from .forms import CrowdfundForm
from fitur_autentikasi.models import Profile


@login_required(login_url="/login/")
def show_crowdfundings(request):
    return render(request, "home.html")


@login_required(login_url="/todolist/login/")
def show_crowdfunding_by_id(request, id):
    return render(request, "crowdfunding_by_id.html")


@login_required(login_url="/todolist/login/")
def create_crowdfund(request):
    form = CrowdfundForm()

    if request.method == "POST":
        form = CrowdfundForm(request.POST)
        if form.is_valid():
            new_crowdfund = form.save(commit=False)
            new_crowdfund.user = Profile.objects.get(user=request.user)
            new_crowdfund.save()
            return redirect("crowdfunding:show_crowdfundings")

    context = {"form": form}
    return render(request, "crowdfund_form.html", context)


@login_required(login_url="/todolist/login/")
def edit_crowdfund(request, id):
    crowdfund = Crowdfund.objects.get(pk=id)
    if crowdfund.user.pk != request.user.pk:
        return redirect("crowdfunding:show_crowdfundings")

    form = CrowdfundForm(instance=crowdfund)

    if request.method == "POST":
        form = CrowdfundForm(request.POST, instance=crowdfund)
        if form.is_valid():
            form.save()
            return redirect("crowdfunding:show_crowdfundings")

    context = {"form": form}
    return render(request, "crowdfund_form.html", context)


@login_required(login_url="/todolist/login/")
def delete_crowdfund(request, id):
    crowdfund = Crowdfund.objects.get(pk=id)
    if crowdfund.user.pk != request.user.pk:
        return redirect("crowdfunding:show_crowdfundings")
    crowdfund.delete()
    return redirect("crowdfunding:show_crowdfundings")


@login_required(login_url="/todolist/login/")
def show_crowdfundings_json(request):
    crowdfunds = Crowdfund.objects.all().order_by("-created")
    return HttpResponse(
        serializers.serialize("json", crowdfunds), content_type="application/json"
    )


@login_required(login_url="/todolist/login/")
def show_crowdfundings_by_id_json(request, id):
    # reference: https://stackoverflow.com/questions/757022/how-do-you-serialize-a-model-instance-in-django
    crowdfund = Crowdfund.objects.get(pk=id)
    data = serializers.serialize(
        "json",
        [
            crowdfund,
        ],
    )
    return HttpResponse(data, content_type="application/json")


@login_required(login_url="/todolist/login/")
def get_user_by_id(request, id):
    profile = Profile.objects.get(user=id)
    user_obj = {
        "username": profile.user.username,
        "first_name": profile.user.first_name,
        "full_name": profile.user.get_full_name(),
        "email": profile.user.email,
        "telephone": profile.telephone,
        "whatsapp": profile.whatsapp,
        "line": profile.line,
    }
    return JsonResponse(user_obj)
