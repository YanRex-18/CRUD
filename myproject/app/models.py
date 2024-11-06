from django.db import models

class producto(models.Model):
    nombre=models.CharField(max_length=100,blank=True)
    descripcion=models.TextField(max_length=200,blank=True)
    precio=models.DecimalField(max_digits=4,decimal_places=2)
    fecha_de_ingreso=models.DateTimeField(auto_now_add=True)


    def __str_(self):
        return self.nombre

