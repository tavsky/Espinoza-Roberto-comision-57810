from django.urls import path
from App1 import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('Empleados/', Empleados, name="Empleados"),
    path('Ventas/', Ventas, name="Ventas"),
    path('Stock/', Stock, name="Stock"),
    path('Clientes/', Clientes, name="Clientes"),
   path('Acerca/', Acerca, name="Acerca"),
    #Formularios

    path('ClientesForm/', ClientesForm, name="ClientesForm"),
    path('EmpleadosForm/', EmpleadoForm, name="EmpleadosForm"),
    path('StockForm/', stockForm, name="StockForm"),
    path('VentasForm/', VentasForm, name="VentasForm"),

        #Buscar

    path('BuscarStock/', BuscarStock, name="BuscarStock"),
    path('EncontrarStock/', EncontrarStock, name="EncontrarStock"),

    #Updates

    path('ClientesUpdate/<id_Clientes>/', ClientesUpdate, name="ClientesUpdate"),
    path('EmpleadosUpdate/<id_Empleado>/', EmpleadoUpdate, name="EmpleadosUpdate"),
    path('StockUpdate/<id_IngresoStock>/', StockUpdate, name="StockUpdate"),
    path('VentasUpdate/<id_IngresoVenta>/', VentasUpdate, name="VentasUpdate"),

    #Delete

    path('ClientesDelete/<id_Clientes>/', ClientesDelete, name="ClientesDelete"),
    path('EmpleadoDelete/<id_Empleado>/', EmpleadoDelete, name="EmpleadoDelete"),
    path('StockDelete/<id_IngresoStock>/', StockDelete, name="StockDelete"),
    path('VentasDelete/<id_IngresoVenta>/', VentasDelete, name="VentasDelete"),

    # Login /Logout / Registration

      path('Login/', loginrequest, name="Login"),
      path('logout/', LogoutView.as_view(template_name="App1/logout.html"), name="logout"),
      path('registro/', register, name="registro"),

    #___ Edición de Perfil / Avatar
    path('perfil/', editProfile, name="perfil"),
    path('password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


]
