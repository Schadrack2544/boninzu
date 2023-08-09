# rentals/models.py
from django.db import models

class Office(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='office_images/')
    owner_contact = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    featured_images = models.ManyToManyField('FeaturedOfficeImage')
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class House(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='house_images/')
    owner_contact = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    featured_images = models.ManyToManyField('FeaturedHouseImage')
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Apartment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='apartment_images/')
    owner_contact = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    featured_images = models.ManyToManyField('FeaturedApartmentImage')
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FeaturedHouseImage(models.Model):
    image = models.ImageField(upload_to='house_images/')
    date_posted=models.DateTimeField(auto_now_add=True)

class FeaturedOfficeImage(models.Model):
    image = models.ImageField(upload_to='office_images/')
    date_posted=models.DateTimeField(auto_now_add=True)

class FeaturedApartmentImage(models.Model):
    image = models.ImageField(upload_to='apartment_images/')
    date_posted=models.DateTimeField(auto_now_add=True)
