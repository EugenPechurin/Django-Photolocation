from PIL.ExifTags import GPSTAGS, TAGS
from django.db import models
from PIL import Image
from django.conf import settings
from photolocation.apps.photolocation_map.exif import get_exif_data


def upload_location(instance, filename):
    return "%s/%s" % (instance.user, filename)


class UploadFile(models.Model):
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.image)

    def get_location(self):
        return get_exif_data(self.image)
