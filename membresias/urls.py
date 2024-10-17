from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from membresias.views import *
from django.contrib.auth.views import LogoutView

app_name = 'membresias'

urlpatterns = [
    url(r'^$',home, name="home"),
    path('loginm/', login_membresias, name="login_membresias"),
    path('verificacionID/', verificacionID, name="verificacionID"),
    path('logout/',LogoutView.as_view(next_page='/'), name='logout'),
    path('registrar_usuarios/',registrar_usuarios, name="registrar_usuarios"),
    path('post_usuarios/',post_usuarios, name="post_usuarios"),
    path('pagar/',pagar, name="pagar"),
    path('pagar_r/',pagar_r, name="pagar_r"),
    path('pago_membresia/',pago_membresia, name="pago_membresia"),
    path('post_pago/',post_pago, name="post_pago"),
    path('verificar_usuario/',verificar_usuario, name="verificar_usuario"),
    path('regresar/',regresar, name="regresar"),
    path('modificar_pago/',modificar_pago, name="modificar_pago"),
    path('renovar/',renovar, name="renovar"),
    path('historial/',historial, name="historial"),
    path('filtros/',filtros, name="filtros"),
    path('eliminarpago/',eliminarpago, name="eliminarpago"),
    path('modificar_historial/',modificar_historial, name="modificar_historial"),
]