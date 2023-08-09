# project/urls.py
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    path('', landing_page, name='landing_page'),
   
    # Add other URLs for your project
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
