from django.db import models

# Create your models here.

#Modelo Documento
class TipoCuenta(models.Model):
    descripcion=models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.descripcion)