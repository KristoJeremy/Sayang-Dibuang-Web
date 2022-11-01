from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from request_barang_bekas.models import Request
from request_barang_bekas.forms import CreateRequestForm
from fitur_autentikasi.models import Profile

def show_requests(request):
    return render(request, "request-barang-bekas.html", {})

@login_required(login_url="/login/")
def create_request(request):
    form = CreateRequestForm()
    if request.method == "POST":
        form = CreateRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.profile = Profile.objects.get(user=request.user)
            new_request.save() 
           
            return redirect("request_barang_bekas:show_requests")

        return JsonResponse({
            "Message": "Request TIDAK Berhasil Dibuat", 
        }, status=500)
    
    context = {"form": form}
    return render(request, "create-request.html", context)

def show_all_requests_json(request):
    list_request = Request.objects.all().order_by("-uploaded_at")
    query = request.GET.get("search")
    if query != "":
        list_request = Request.objects.filter(nama_barang__icontains=query).order_by("-uploaded_at")

    return HttpResponse(serializers.serialize("json", list_request))

def show_request_details(request, id):
    curRequest = Request.objects.select_related("profile").select_related("user").get(id=id)
    user = request.user 

    context = {
        "curRequest": curRequest,
        "user": user
    }
    return render(request, "request-details.html", context)

@login_required(login_url="/login/")
def edit_request(request, id):
    context = {}
 
    obj = get_object_or_404(Request, id=id, user=request.user)

    form = CreateRequestForm(request.POST or None, request.FILES or None, instance=obj)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/request/"+str(id))
 
    context["form"] = form
 
    return render(request, "request-edit.html", context)

@login_required(login_url="/login/")
def delete_request(request, id):
    curRequest = Request.objects.get(user=request.user, id=id)
    curRequest.delete()
    return HttpResponseRedirect(reverse("request_barang_bekas:show_requests"))