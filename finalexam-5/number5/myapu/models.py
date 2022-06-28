from django.db import models

# Create your models here.
class loginaccount(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)

class registeraccount(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)

class product(models.Model):
    productid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
