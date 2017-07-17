from django.contrib import admin
from .models import UploadFile


# Register your models here.

class UploadFileAdmin(admin.ModelAdmin):
    list_display = ["file", "timestamp"]
    list_filter = ["timestamp"]

    class Meta:
        model = UploadFile


admin.site.register(UploadFile)
