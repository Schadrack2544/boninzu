# rentals/views.py
from django.shortcuts import get_object_or_404, render
from .models import Office, House, Apartment

def landing_page(request):
    offices = Office.objects.all()
    houses = House.objects.all()
    apartments = Apartment.objects.all()
    return render(request, 'landing_page.html', {'offices': offices, 'houses': houses, 'apartments': apartments})

def office_list(request):
    offices = Office.objects.all()
    return render(request, 'office_list.html', {'offices': offices})

def office_detail(request,pk):
    office=get_object_or_404(Office,pk=pk)
    return render(request, 'office_detail.html', {'office': office})

def house_list(request):
    houses = House.objects.all()
    return render(request, 'house_list.html', {'houses': houses})

def house_detail(request,pk):
    house=get_object_or_404(House,pk=pk)
    return render(request, 'house_detail.html', {'house': house})

def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartment_list.html', {'apartments': apartments})

def apartment_detail(request,pk):
    apartment=get_object_or_404(Apartment,pk=pk)
    return render(request, 'apartment_detail.html', {'apartment': apartment})

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    return render(request, 'contact.html',{})
