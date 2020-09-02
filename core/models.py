from django.db import models

"""------------------------------------------------------------"""
class Venta(models.Model):
    id = models.CharField(max_length = 50, primary_key=True)
    fecha = models.DateField()
    monto_final = models.IntegerField()
    cantidad = models.IntegerField(default= 0)
    Cliente = models.ForeignKey('Cliente', on_delete = models.CASCADE, default = None,)
    descuento = models.IntegerField()

    def DescApli(self):
        return (self.Descuento)
    DescApli.boolean = True
    DescApli.short_description = 'tiene descuento'

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return ("ID: {} | {} | {} ".format(self.id, self.fecha, self.monto_final))

class Producto(models.Model):
    id = models.CharField(max_length = 50, primary_key=True)
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField()
    stock = models.IntegerField()


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return ("ID: {} | {} | {}".format(self.id, self.nombre,self.precio))

class Categoria(models.Model):
    id = models.CharField(max_length = 50, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Caegorias"

    def __str__(self):
        return ("ID: {} | {} | {}".format(self.id, self.nombre, self.descripcion))

"""------------------------------------------------------------"""
class Cliente(models.Model):
    nombre = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    RUT = models.CharField(max_length=50)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return ("ID: {} | {} | {} | {}".format(self.id, self.nombre, self.telefono, self.RUT))

class Proveedor(models.Model):
    telefono = models.IntegerField()
    RUT = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    web = models.CharField(max_length=50)
    Producto = models.ForeignKey('Producto', on_delete=models.CASCADE, default=None, )

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return ("ID: {} | {} | {} | {}".format(self.id, self.nombre, self.telefono, self.RUT))

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "direcciones"

    def __str__(self):
        return ("ID: {} | {} {} | {}".format(self.id, self.calle, self.numero, self.ciudad))