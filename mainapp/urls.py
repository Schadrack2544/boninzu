# project/urls.py
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('office/<int:pk>/',office_detail, name='office-detail'),
    path('offices/', office_list, name='office_list'),
    path('houses/', house_list, name='house_list'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('house/<int:pk>/', house_detail, name='house_detail'),
    path('apartments/', apartment_list, name='apartment_list'),
    path('apartment/<int:pk>/',apartment_detail, name='apartment_detail'),
    # Add other URLs for your project
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
