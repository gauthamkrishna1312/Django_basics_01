from django.db import models


# Create your models here.

class Book(models.Model):
    tittle = models.CharField(max_length=50, blank=True, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(decimal_places=5, max_digits=10, blank=False)
    docs = models.FileField(blank=True)
