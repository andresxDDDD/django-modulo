from django.contrib import admin
from .models import Producto, cerveza

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(cerveza)
class cervezaAdmin(admin.ModelAdmin):
    pass
