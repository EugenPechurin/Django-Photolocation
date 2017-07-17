from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from PIL import Image
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib import auth
from photolocation.apps.photolocation_map.exif import get_exif_data, get_lat_lon
from photolocation.apps.photolocation_map.forms import UploadFileForm
from photolocation.apps.photolocation_map.models import UploadFile
from django.utils import timezone


def index(request):
    if request.user.is_authenticated:
        photos = UploadFile.objects.filter(user=request.user)
        print(photos)
        context = {
            "photos": photos,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html', {'username': auth.get_user(request).username})


# @csrf_exempt

def search(request):
    if request.method == "POST":
        image = Image.open(request.FILES['file'])
        exif_data = get_exif_data(image)
        gps = get_lat_lon(exif_data)
        if gps[0] != 'None':
            return JsonResponse({"latitude": gps[0], "longitude": gps[1]})
        return JsonResponse({"Error": "Error"})


def addphoto(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.timestamp = timezone.now()
            instance.save()
        image = Image.open(request.FILES['file'])
        exif_data = get_exif_data(image)
        gps = get_lat_lon(exif_data)
        if gps[0] != 'None':
            return JsonResponse({"latitude": gps[0], "longitude": gps[1]})
        return JsonResponse({"Error": "Error"})
    form = UploadFileForm()
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)
