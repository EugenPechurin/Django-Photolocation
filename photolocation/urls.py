"""photolocation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from photolocation.apps.photolocation_map import urls
# from django.contrib.sitemaps.views import sitemap
# from photologue.sitemaps import GallerySitemap, PhotoSitemap
from django.conf import settings
from django.conf.urls.static import static
from photolocation.apps.gallery import views as gallery

# sitemaps = {
# 'photologue_galleries': GallerySitemap,
# 'photologue_photos': PhotoSitemap,
# }

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gallery/', gallery.gallery, name='gallery'),
    url(r'^auth/', include('photolocation.apps.loginsys.urls')),
    # url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'),
    url(r'', include('photolocation.apps.photolocation_map.urls'))
]

if settings.DEBUG:
    pass
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)