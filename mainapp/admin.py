from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Office)
admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(FeaturedApartmentImage)
admin.site.register(FeaturedHouseImage)
admin.site.register(FeaturedOfficeImage)