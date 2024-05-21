from django.db import models

# Create your models here.

class BazaItem(models.Model):
    title = models.CharField(max_length=50)
    cena = models.FloatField()
    dostepne = models.BooleanField(default=False)
    adres = models.CharField(max_length=100)
    opis = models.CharField(max_length=100, default='123')
    
    
