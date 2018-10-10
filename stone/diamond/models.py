from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class image(models.Model):
    url = models.CharField(max_length=50)
    image_type = models.CharField(max_length=50)

class rings(models.Model):
    url = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    diamond_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gold_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class bangles(models.Model):
    url = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    diamond_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gold_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class earrings(models.Model):
    url = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    diamond_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gold_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class necklaces(models.Model):
    url = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    diamond_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gold_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class pendants(models.Model):
    url = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    diamond_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gold_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


class contact(models.Model):
    name = models.CharField(max_length=50)
    #contact_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Contact number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #number = models.CharField(validators=[contact_regex], max_length=15)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.CharField(max_length=500)