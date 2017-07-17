from django.http import Http404
from django.shortcuts import render, get_object_or_404
from photolocation.apps.photolocation_map.models import UploadFile
from django.contrib import auth


# Create your views here.

def gallery(request):
    if request.user.is_authenticated:
        photos = UploadFile.objects.filter(user=request.user)
        print(photos)
        context = {
        "photos": photos,
        }
        return render(request, 'gallery.html', context)
    raise Http404
