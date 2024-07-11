from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class ClienteForm(forms.Form):
    Nombre=forms.CharField(max_length=40,required=True)
    email=forms.EmailField(required=True)
    Direccion=forms.CharField(max_length=70,required=True)
    Fecha_Nacimiento=forms.DateField()

class EmpleadosForm(forms.Form):
    Nombre=forms.CharField(max_length=40,required=True)
    Cargo=forms.ChoiceField(choices=[('Vendedor', 'Vendedor'),('Encargado de tienda', 'Encargado de tienda'),('Gerente Zona', 'Gerente Zona')], required=True) 


class StockForm(forms.Form):
    SKU=forms.CharField(max_length=50)
    Cantidad=forms.CharField(max_length=50)
    Nombre_encargado=forms.CharField(max_length=50)
    Nombre_Producto=forms.CharField(max_length=80)
class VentaForm(forms.Form):
    SKU=forms.CharField(max_length=50)
    Cantidad=forms.CharField(max_length=50)
    Nombre_encargado=forms.CharField(max_length=50)
    Precio=forms.CharField(max_length=50)
    Cliente=forms.CharField(max_length=50)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=60, required=True)
    last_name = forms.CharField(label="Apellido", max_length=60, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)