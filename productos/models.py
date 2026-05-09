from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

class cerveza(models.Model):
    nombre = models.CharField(max_length=100)
    tipo =  models.CharField(max_length=100)
    grados =  models.CharField(max_length=100)
    
    
