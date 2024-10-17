from multiprocessing.sharedctypes import Value
from django import forms
from .models import *
from django.utils import timezone

class Productoform(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        
class HistorialVentaForm(forms.Form):
    fecha = models.DateField(default=timezone.now) 
    id_producto = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    cantidad = forms.IntegerField()
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    subtotal = forms.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = forms.CharField(max_length=100)
    total = forms.DecimalField(max_digits=10, decimal_places=2)


    def clean_id_producto(self):
        id_producto = self.cleaned_data['id_producto']
        # Agrega tus validaciones personalizadas para el ID del producto
        if not id_producto:
            raise forms.ValidationError("El ID del producto es requerido.")
        return id_producto