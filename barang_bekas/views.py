
import json
from mimetypes import init
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from barang_bekas.models import Barang
from django.shortcuts import HttpResponse, render, redirect
from django.core import serializers
from django.http.response import JsonResponse
from barang_bekas.forms import CreateBarangForm
import cloudinary
from barang_bekas.models import Barang, Kategori, Lokasi
from fitur_autentikasi.models import Profile
from django.urls import reverse

# Create your views here.
# 1. add barang 
def create_barang(request):
    # protect page
    if not request.user.is_authenticated:
        return redirect("/login/") 
    form = CreateBarangForm()

    if request.method=="POST":
        form = CreateBarangForm(request.POST, request.FILES)
        if form.is_valid():
            new_barang = form.save(commit=False)
            new_barang.user = request.user
            new_barang.profile = Profile.objects.get(user=request.user)
            new_barang.save() 
            # return JsonResponse({
            #     "Message": "Item Berhasil Dibuat", 
            # },status=201)
            return redirect('barang_bekas:show_barang')

        return JsonResponse({
            "Message": "Item TIDAK Berhasil Dibuat", 
        },status=500)
    context = {'form':form}
    return render(request, 'upload.html', context)

# 2. get barang
def show_barang(request):
     # protect page
    if not request.user.is_authenticated:
        return redirect("/login/") 
    context = {}
    return render(request, 'barang-bekas.html', context)

def show_barang_detail(request, id):
     # protect page
    if not request.user.is_authenticated:
        return redirect("/login/") 
    barang = Barang.objects.select_related('profile').select_related('user').get(id=id)
    user = request.user 

    context = {
        'barang':barang,
        'user':user
    }
    return render(request, 'barang-details.html', context)

def get_all_barang_json(request):
    list_barang = Barang.objects.all().select_related('user').order_by('-uploaded_at')
    return HttpResponse(serializers.serialize('json', list_barang)) 
    # return HttpResponse(serializers.serialize('json', [x.user for x in list_barang])) # error

def get_one_barang_json(request, id):
    barang = Barang.objects.get(pk=id)
    return HttpResponse(serializers.serialize("json", barang), content_type="application/json")

# 3. edit barang (ref: https://www.geeksforgeeks.org/update-view-function-based-views-django/)
def edit_barang(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Barang, id = id, user=request.user)

    form = CreateBarangForm(request.POST or None, request.FILES or None, instance=obj)
    
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/barang/"+str(id))
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "barang-edit.html", context)

# 4. delete barang
def delete_barang(request, id):
    barang = Barang.objects.get(user=request.user, id=id)
    barang.delete()
    return HttpResponseRedirect(reverse("barang_bekas:show_barang"))

# bikin modal buat add category & lokasii?? tapi gabisa edit/delete (masi mikir )
# 5. add kategori
def create_kategori(request):
    if request.method=="POST":
        jenis = request.POST.get('jenis').capitalize()
        item = Kategori(jenis=jenis)
        item.save()
        response = {
            "Message": "Kategori Berhasil Dibuat",
            "id":item.pk,
            "jenis": item.jenis
        }
        return JsonResponse(response,status=200)


# 6. add lokasi
def create_lokasi(request):
    if request.method=="POST":
        nama = request.POST.get('nama').capitalize()
        item = Lokasi(nama=nama)
        item.save()
        response = {
            "Message": "Lokasi Berhasil Dibuat",
            "id":item.pk,
            "nama": item.nama
        }
        return JsonResponse(response,status=200)
