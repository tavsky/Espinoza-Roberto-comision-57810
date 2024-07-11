from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cliente)
admin.site.register(IngresoStock)
admin.site.register(IngresoVenta)
admin.site.register(Empleado)