from django.db import models
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True) # Campo para el ID del producto, con auto-incremento
    id_producto = models.CharField(max_length=20,unique=True)
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=70)   

class Venta(models.Model):
    idhistorial = models.IntegerField()
    id_producto = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    # Agrega más campos según tus necesidades
   
class HistorialVenta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=None)  # Guarda la fecha actual al crear el registro
    productosv = models.CharField(max_length=1000)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)