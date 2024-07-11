from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy

from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, "App1/index.html")
@login_required
def Empleados(request):
    contexto={"Empleados":Empleado.objects.all() }
    return render(request, "App1/Empleados.html",contexto)

def Acerca(request):
    return render(request, "App1/Acerca.html")

@login_required
def Stock(request):
    contexto={"Stock":IngresoStock.objects.all() }
    return render(request, "App1/Stock.html", contexto)
@login_required
def Clientes(request):
    contexto={"Clientes":Cliente.objects.all() }
    return render(request, "App1/Clientes.html", contexto)
@login_required
def Ventas(request):
    contexto={"Ventas":IngresoVenta.objects.all() }
    return render(request, "App1/Ventas.html", contexto)

# Formularios
@login_required
def ClientesForm(request):
    if request.method == "POST":
        FormularioCliente=ClienteForm(request.POST)
        if FormularioCliente.is_valid():
            Cliente_Nombre=FormularioCliente.cleaned_data.get("Nombre")
            Cliente_Email=FormularioCliente.cleaned_data.get("email")
            Cliente_Direccion=FormularioCliente.cleaned_data.get("Direccion")
            Cliente_Fecha_Nacimiento=FormularioCliente.cleaned_data.get("Fecha_Nacimiento")        
            cliente=Cliente(Nombre=Cliente_Nombre, email=Cliente_Email,direccion=Cliente_Direccion,Fecha_Nacimiento=Cliente_Fecha_Nacimiento)
            cliente.save()
            contexto={"Clientes": Cliente.objects.all() }
            return render(request, "App1/Clientes.html", contexto)
    
    else:
        FormularioCliente = ClienteForm()

    return render (request,"App1/ClientesForm.html", {"form":FormularioCliente})
@login_required
def EmpleadoForm(request):
    if request.method == "POST":
        FormularioEmpleado=EmpleadosForm(request.POST)
        if FormularioEmpleado.is_valid():
            Empleado_Nombre=FormularioEmpleado.cleaned_data.get("Nombre")
            Empleado_Cargo=FormularioEmpleado.cleaned_data.get("Cargo")    
            empleado=Empleado(Nombre=Empleado_Nombre, Cargo=Empleado_Cargo)
            empleado.save()
            contexto={"Empleados": Empleado.objects.all() }
            return render(request, "App1/Empleados.html", contexto)
    
    else:
        FormularioEmpleado = EmpleadosForm()

    return render (request,"App1/EmpleadosForm.html", {"form":FormularioEmpleado})
@login_required
def stockForm(request):
    if request.method == "POST":
        FormularioStock=StockForm(request.POST)
        if FormularioStock.is_valid():
            Stock_SKU=FormularioStock.cleaned_data.get("SKU")
            Stock_Cantidad=FormularioStock.cleaned_data.get("Cantidad")
            Stock_Nombre_encargado=FormularioStock.cleaned_data.get("Nombre_encargado")      
            Stock_Nombre_Producto=  FormularioStock.cleaned_data.get("Nombre_Producto")  
            stock=IngresoStock(SKU=Stock_SKU, Cantidad=Stock_Cantidad,Nombre_encargado=Stock_Nombre_encargado,Nombre_Producto=Stock_Nombre_Producto)
            stock.save()
            contexto={"Stock": IngresoStock.objects.all() }
            return render(request, "App1/Stock.html", contexto)
    
    else:
        FormularioStock = StockForm()

    return render (request,"App1/StockForm.html", {"form":FormularioStock})
@login_required
def VentasForm(request):
    if request.method == "POST":
        FormularioVentas=VentaForm(request.POST)
        if FormularioVentas.is_valid():
            Ventas_SKU=FormularioVentas.cleaned_data.get("SKU")
            Ventas_Cantidad=FormularioVentas.cleaned_data.get("Cantidad")
            Ventas_Nombre_encargado=FormularioVentas.cleaned_data.get("Nombre_encargado")   
            Ventas_Precio=FormularioVentas.cleaned_data.get("Precio")   
            Ventas_Cliente=FormularioVentas.cleaned_data.get("Cliente")     
            venta=IngresoVenta(SKU=Ventas_SKU, Cantidad=Ventas_Cantidad,Nombre_encargado=Ventas_Nombre_encargado,Precio=Ventas_Precio,Cliente=Ventas_Cliente)
            venta.save()
            contexto={"Ventas": IngresoVenta.objects.all() }
            return render(request, "App1/Ventas.html", contexto)
    
    else:
        FormularioVentas = VentaForm()

    return render (request,"App1/VentasForm.html", {"form":FormularioVentas})

#Busquedas
@login_required
def BuscarStock(request):
    return render(request, "App1/BuscarStock.html")
@login_required
def EncontrarStock(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        Stock=IngresoStock.objects.filter(SKU=patron)
        contexto={'Stock':Stock}
    else:
        contexto={'Stock':IngresoStock.objects.all()}
    return render(request, "App1/Stock.html", contexto)

#updates
@login_required
def StockUpdate(request,id_IngresoStock):
    stock=IngresoStock.objects.get(id=id_IngresoStock)
    if request.method == "POST":
        FormularioStock=StockForm(request.POST)
        if FormularioStock.is_valid():
            stock.SKU=FormularioStock.cleaned_data.get("SKU")
            stock.Cantidad=FormularioStock.cleaned_data.get("Cantidad")
            stock.Nombre_encargado=FormularioStock.cleaned_data.get("Nombre_encargado")      
            stock.Nombre_Producto=  FormularioStock.cleaned_data.get("Nombre_Producto")  
            stock.save()
            contexto={"Stock": IngresoStock.objects.all() }
            return render(request, "App1/Stock.html", contexto)
    else:
        stockForm= StockForm(initial={"SKU":stock.SKU,"Cantidad":stock.Cantidad,"Nombre_encargado":stock.Nombre_encargado,"Nombre_Producto":stock.Nombre_Producto})

    return render(request,"App1/StockForm.html", {"form":stockForm})
@login_required
def EmpleadoUpdate(request,id_Empleado):
    empleado=Empleado.objects.get(id=id_Empleado)
    if request.method == "POST":
        FormularioEmpleado=EmpleadosForm(request.POST)
        if FormularioEmpleado.is_valid():
            empleado.Nombre=FormularioEmpleado.cleaned_data.get("Nombre")
            empleado.Cargo=FormularioEmpleado.cleaned_data.get("Cargo")    
            empleado.save()
            contexto={"Empleados": Empleado.objects.all() }
            return render(request, "App1/Empleados.html", contexto)
    else:
        empleadosForm= EmpleadosForm(initial={"Nombre":empleado.Nombre,"Cargo":empleado.Cargo})

    return render(request,"App1/EmpleadosForm.html", {"form":empleadosForm})
@login_required
def ClientesUpdate(request,id_Clientes):
    cliente=Cliente.objects.get(id=id_Clientes)
    if request.method == "POST":
        FormularioCliente=ClienteForm(request.POST)
        if FormularioCliente.is_valid():
            cliente.Nombre=FormularioCliente.cleaned_data.get("Nombre")
            cliente.email=FormularioCliente.cleaned_data.get("email")
            cliente.direccion=FormularioCliente.cleaned_data.get("Direccion")
            cliente.Fecha_Nacimiento=FormularioCliente.cleaned_data.get("Fecha_Nacimiento")        
            cliente.save()
            contexto={"Clientes": Cliente.objects.all() }
            return render(request, "App1/Clientes.html", contexto)
    else:
        clienteForm= ClienteForm(initial={"Nombre":cliente.Nombre,"email":cliente.email,"Direccion":cliente.direccion,"Fecha_Nacimiento":cliente.Fecha_Nacimiento})

    return render(request,"App1/ClientesForm.html", {"form":clienteForm})
@login_required
def VentasUpdate(request,id_IngresoVenta):
    Venta=IngresoVenta.objects.get(id=id_IngresoVenta)
    if request.method == "POST":
        FormularioVentas=VentaForm(request.POST)
        if FormularioVentas.is_valid():
            Venta.SKU=FormularioVentas.cleaned_data.get("SKU")
            Venta.Cantidad=FormularioVentas.cleaned_data.get("Cantidad")
            Venta.Nombre_encargado=FormularioVentas.cleaned_data.get("Nombre_encargado")   
            Venta.Precio=FormularioVentas.cleaned_data.get("Precio")   
            Venta.Cliente=FormularioVentas.cleaned_data.get("Cliente")     
            Venta.save()
            contexto={"Ventas": IngresoVenta.objects.all() }
            return render(request, "App1/Ventas.html", contexto)
    else:
        ventasForm= VentaForm(initial={"SKU":Venta.SKU,"Cantidad":Venta.Cantidad,"Nombre_encargado":Venta.Nombre_encargado,"Precio":Venta.Precio,"Cliente":Venta.Cliente})

    return render(request,"App1/VentasForm.html", {"form":ventasForm})


#Borrar
@login_required
def StockDelete(request,id_IngresoStock):
    stock=IngresoStock.objects.get(id=id_IngresoStock)
    stock.delete()
    contexto={"Stock": IngresoStock.objects.all() }
    return render(request, "App1/Stock.html", contexto)
@login_required
def EmpleadoDelete(request,id_Empleado):
    empleado=Empleado.objects.get(id=id_Empleado)
    empleado.delete()
    contexto={"Empleados": Empleado.objects.all() }
    return render(request, "App1/Empleados.html", contexto)
@login_required
def ClientesDelete(request,id_Clientes):
    cliente=Cliente.objects.get(id=id_Clientes)
    cliente.delete()
    contexto={"Clientes": Cliente.objects.all() }
    return render(request, "App1/Clientes.html", contexto)
@login_required
def VentasDelete(request,id_IngresoVenta):
    Venta=IngresoVenta.objects.get(id=id_IngresoVenta)
    Venta.delete()
    contexto={"Ventas": IngresoVenta.objects.all() }
    return render(request, "App1/Ventas.html", contexto)

#Login / Logout / Register

def loginrequest(request):
    if request.method == "POST":
        if request.method == "POST":
            usuario = request.POST["username"]
            clave = request.POST["password"]
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return render(request, "App1/index.html")
            else:
                return redirect(reverse_lazy('login'))
    else:
        miform = AuthenticationForm()
    return render(request,"App1/Login.html", {"form":miform})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "App1/Registro.html", {"form": miForm}) 

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "App1/editarPerfil.html", {"form": miForm})
    
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "App1/cambiar_clave.html"
    success_url = reverse_lazy("home")



@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "App1/agregarAvatar.html", {"form": miForm})    