from django.db import models

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, default=None)
    primer_apellido = models.CharField(max_length=70, blank=False, default=None)
    segundo_apellido = models.CharField(max_length=70, blank=False, default=None)
    correo = models.CharField(max_length=70, blank=False, default=None)
    telefono = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.nombre

class pago(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_pago = models.DateField(default=None)
    id_cliente = models.IntegerField(default=None)
    fecha_limite = models.DateField(default=None)
    precio_pago = models.FloatField(default=None)
    metodo = models.CharField(max_length=20, blank=False, default=None)
    subtotal = models.FloatField(default=None)
    iva = models.FloatField(default=None)
