

# Create your models here.
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural ='Categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(Categoria, related_name="productos", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    precio = models.FloatField()
    descripcion = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural ='Productos'
        ordering = ['-created']

    def __str__(self):
        return self.nombre
