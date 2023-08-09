# project/urls.py
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    #path('for-sale/', include('forsales.urls'),name="for_sales")
    # Add other URLs for your project
]
