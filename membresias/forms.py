from multiprocessing.sharedctypes import Value
from django import forms
from .models import *

class clienteform(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class pagoform(forms.ModelForm):
    class Meta:
        model = pago
        fields = '__all__'