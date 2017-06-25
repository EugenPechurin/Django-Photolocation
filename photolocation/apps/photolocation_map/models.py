from PIL.ExifTags import GPSTAGS, TAGS
from django.db import models
from PIL import Image
# Create your models here.

class UploadFile(models.Model):

    file = models.ImageField(upload_to="image/")

    def __str__(self):
        return str(self.file)
