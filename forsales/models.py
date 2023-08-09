from django.db import models

# Create your models here.
class HouseToSale(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='houses_to_sale/')
    owner_contact = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    featured_images = models.ManyToManyField('FeaturedHouseToSaleImage')
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class FeaturedHouseToSaleImage(models.Model):
    image = models.ImageField(upload_to='house_images/')
    date_posted=models.DateTimeField(auto_now_add=True)
