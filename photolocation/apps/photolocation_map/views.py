from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
# Create your views here.
from PIL import Image
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib import auth
from photolocation.apps.photolocation_map.exif import get_exif_data, get_lat_lon
from photolocation.apps.photolocation_map.forms import UploadFileForm
from photolocation.apps.photolocation_map.models import UploadFile


def index(request):
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
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return JsonResponse({"answear": "Ok"})
    form = UploadFileForm()
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)
