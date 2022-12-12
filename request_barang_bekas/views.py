from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import datetime
from request_barang_bekas.models import Request, RequestMobile
from barang_bekas.models import Kategori
from request_barang_bekas.forms import CreateRequestForm
from fitur_autentikasi.models import Profile

def show_request(request):
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

@csrf_exempt
def create_request_ajax(request):
    if request.method == "POST":
        body = request.POST
        username = body.get('username')

        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        nama_barang = body.get('nama_barang')
        deskripsi = body.get('deskripsi')
        kategori_jenis = body.get('kategori')
        kategori = Kategori.objects.get(jenis= kategori_jenis)
        item = RequestMobile(profile=profile, nama_barang=nama_barang, deskripsi=deskripsi, uploaded_at=datetime.datetime.now(), kategori=kategori, available=True)
        item.save()
        
        return JsonResponse({"message":"Berhasil mengupload request!"})

def get_all_request_json(request):
    list_request = Request.objects.all().order_by("-uploaded_at")
    query = request.GET.get("search")
    if query != "":
        list_request = Request.objects.filter(nama_barang__icontains=query).order_by("-uploaded_at")

    return HttpResponse(serializers.serialize("json", list_request))

def get_all_request_mobile(request):
    list_request = RequestMobile.objects.select_related('profile').select_related('profile__user').all().order_by('-uploaded_at')

    return HttpResponse(serializers.serialize('json', list_request))

def get_owner_request(request, id):
    owner = Profile.objects.get(pk=id)

    return HttpResponse(serializers.serialize("json", [owner]), content_type="application/json")

def get_one_request_json(request, id):
    cur_request = Request.objects.get(pk=id)
    return HttpResponse(serializers.serialize("json", cur_request), content_type="application/json")

def show_request_detail(request, id):
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

def edit_request_ajax(request, id):
    if request.method == "POST":
        body = request.POST

        cur_request = RequestMobile.objects.get(pk=id)

        nama_barang = body.get('nama_barang')
        deskripsi = body.get('deskripsi')
        kategori_jenis = body.get('kategori')
        kategori = Kategori.objects.get(jenis= kategori_jenis)
        available = body.get('available')

        cur_request.nama_barang = nama_barang
        cur_request.deskripsi = deskripsi
        cur_request.kategori = kategori
        cur_request.available = available

        cur_request.save()

        return JsonResponse({"message":"Berhasil mengupdate request!"})

@login_required(login_url="/login/")
def delete_request(request, id):
    curRequest = Request.objects.get(user=request.user, id=id)
    curRequest.delete()
    return HttpResponseRedirect(reverse("request_barang_bekas:show_requests"))

@csrf_exempt
def delete_request_mobile(request, id):

    cur_request = RequestMobile.objects.get(id=id)
    cur_request.delete()
    return JsonResponse({"message":"Berhasil menghapus request!"})