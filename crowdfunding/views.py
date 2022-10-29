from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from fitur_autentikasi.models import Profile
from .models import Crowdfund
from .forms import CrowdfundForm


@login_required(login_url="/login/")
def show_crowdfundings(request):
    return render(request, "home.html")


@login_required(login_url="/login/")
def show_crowdfunding_by_id(request, id):
    return render(request, "crowdfunding_by_id.html")


@login_required(login_url="/login/")
def create_crowdfund(request):
    CREATE_POINT = 10
    form = CrowdfundForm()

    if request.method == "POST":
        form = CrowdfundForm(request.POST)
        if form.is_valid():
            received = request.POST["received"]
            target = request.POST["target"]
            new_crowdfund = form.save(commit=False)
            new_crowdfund.user = Profile.objects.get(user=request.user)
            new_crowdfund.user.add_poin(CREATE_POINT)
            if received == target:
                new_crowdfund.is_accomplished = True
            new_crowdfund.save()
            return redirect("crowdfunding:show_crowdfundings")

    context = {"form": form}
    return render(request, "crowdfund_form.html", context)


@login_required(login_url="/login/")
def edit_crowdfund(request, id):
    crowdfund = Crowdfund.objects.get(pk=id)
    if crowdfund.user.user.id != request.user.id:
        return redirect("crowdfunding:show_crowdfundings")

    form = CrowdfundForm(instance=crowdfund)

    if request.method == "POST":
        form = CrowdfundForm(request.POST, instance=crowdfund)
        if form.is_valid():
            received = request.POST["received"]
            target = request.POST["target"]
            edited_crowdfund = form.save(commit=False)
            if received == target:
                edited_crowdfund.is_accomplished = True
            else:
                edited_crowdfund.is_accomplished = False
            edited_crowdfund.save()
            return redirect("crowdfunding:show_crowdfundings")

    context = {"form": form}
    return render(request, "crowdfund_form.html", context)


@login_required(login_url="/login/")
def delete_crowdfund(request, id):
    crowdfund = Crowdfund.objects.get(pk=id)
    if crowdfund.user.user.id == request.user.id:
        crowdfund.delete()
        crowdfunds = Crowdfund.objects.all()
        return HttpResponse(
            serializers.serialize("json", crowdfunds), content_type="application/json"
        )

    return HttpResponseBadRequest("Gagal menghapus crowdfund.")


@login_required(login_url="/login/")
def show_crowdfundings_json(request):
    crowdfunds = Crowdfund.objects.all().order_by("-created").values()
    obj = []
    for c in crowdfunds:
        c["profile"] = list(Profile.objects.filter(user__id=c["user_id"]).values())[0]
        c["profile"].pop("user_id")
        c["profile"]["user"] = list(User.objects.filter(pk=c["user_id"]).values())[0]
        c["profile"]["user"].pop("password")
        c["profile"]["user"].pop("last_login")
        c["profile"]["user"].pop("is_superuser")
        c["profile"]["user"].pop("is_staff")
        c["profile"]["user"].pop("is_active")
        c["profile"]["user"].pop("date_joined")
        obj.append(c)
    return JsonResponse(obj, safe=False)


@login_required(login_url="/login/")
def show_crowdfundings_by_id_json(request, id):
    c = Crowdfund.objects.filter(pk=id).values()[0]
    c["profile"] = list(Profile.objects.filter(user__id=c["user_id"]).values())[0]
    c["profile"].pop("user_id")
    c["profile"]["user"] = list(User.objects.filter(pk=c["user_id"]).values())[0]
    c["profile"]["user"].pop("password")
    c["profile"]["user"].pop("last_login")
    c["profile"]["user"].pop("is_superuser")
    c["profile"]["user"].pop("is_staff")
    c["profile"]["user"].pop("is_active")
    c["profile"]["user"].pop("date_joined")

    return JsonResponse(c, safe=False)


@login_required(login_url="/login/")
def add_point_when_contacting(request, id):
    CONTACT_POINT = 5
    crowdfund = Crowdfund.objects.get(pk=id)

    if crowdfund.user.user.id == request.user.id:
        return JsonResponse({"message": "Anda tidak bisa menghubungi diri sendiri."})

    if Crowdfund.objects.filter(pk=id, helpers__user=request.user):
        return JsonResponse(
            {"message": "Terima kasih telah bersedia membantu."},
        )

    user_profile = Profile.objects.get(user=request.user)
    crowdfund.helpers.add(user_profile)
    user_profile.add_poin(CONTACT_POINT)
    return JsonResponse(
        {
            "message": "Terima kasih telah bersedia membantu. Kamu mendapatkan 5 poin!",
            "poin": user_profile.poin,
        },
    )
