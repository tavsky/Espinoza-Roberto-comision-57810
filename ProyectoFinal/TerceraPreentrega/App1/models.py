from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IngresoStock(models.Model):
    SKU=models.CharField(max_length=50)
    Cantidad=models.CharField(max_length=50)
    Nombre_encargado=models.CharField(max_length=50)
    Nombre_Producto=models.CharField(max_length=80)
    def __str__(self):
        return f"{self.SKU},{self.Cantidad},{self.Nombre_encargado},{self.Nombre_Producto}"

class Cliente(models.Model):
    Nombre=models.CharField(max_length=40)
    email=models.EmailField()
    direccion=models.CharField(max_length=70)
    Fecha_Nacimiento=models.DateField()
    def __str__(self):
     return f"{self.Nombre},{self.email}"

class Empleado(models.Model):
    Nombre=models.CharField(max_length=50)
    CARGO_CHOICES = [('Vendedor', 'Vendedor'),('Encargado de tienda', 'Encargado de tienda'),('Gerente Zona', 'Gerente Zona')]
    Cargo=models.CharField(max_length=50, choices=CARGO_CHOICES)      
    def __str__(self):
        return f"{self.Nombre},{self.Cargo}"
class IngresoVenta(models.Model):
    SKU=models.CharField(max_length=50)
    Cantidad=models.CharField(max_length=50)
    Nombre_encargado=models.CharField(max_length=50)
    Precio=models.CharField(max_length=50)
    Cliente=models.CharField(max_length=60)
    def __str__(self):
     return f"{self.SKU},{self.Cantidad},{self.Nombre_encargado},{self.Precio},{self.Cliente}"
    
class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   