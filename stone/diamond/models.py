from django.db import models

# Create your models here.
class image(models.Model):
    url = models.CharField(max_length=50)
    image_type = models.CharField(max_length=50)

class rings(models.Model):
    url = models.CharField(max_length=50)
    price = models.CharField(max_length=100)

class bangles(models.Model):
    url = models.CharField(max_length=50)
    price = models.CharField(max_length=100)

class contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=500)