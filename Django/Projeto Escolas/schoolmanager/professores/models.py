from django.db import models

# Create your models here.
class Professor(models.Model):
    primero_nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    area_de_estudo = models.CharField()