from django.contrib import admin
from core.models import *
### 3), 6) y 8) -----------------------------------------------------###
class ClienteAdmin(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Venta
    inlines = [EntryInLines,]
    list_display = ['RUT', 'nombre', 'telefono']
    search_fields = ('nombre','RUT','telefono')
### 4) y 7) -----------------------------------------------------###
class ProveedorInLine(admin.TabularInline):
    model=Proveedor
    extra = 2
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines =[ProveedorInLine]
    fieldsets = (
        ('Descripcion', {'fields': ('id', 'nombre')}),
        ('Variables', {'fields': ('precio', 'stock',)}),)
### 5)      -----------------------------------------------------###
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['web', 'nombre', 'telefono']
    search_fields= ('nombre','RUT')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Direccion)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Categoria)