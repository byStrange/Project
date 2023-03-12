from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20)
    image_file = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.name