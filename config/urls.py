from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, "base.html", {})

urlpatterns = [
    path('', index, name="home"),
    path('products/', include('apps.product.urls')),
    path('auth/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )