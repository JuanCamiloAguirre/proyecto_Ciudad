from django.db import models
from apps.cuenta.models import Cuenta

# Create your models here.

class Cliente(models.Model):
   
    cedula=models.CharField(max_length=10, primary_key=True)
    nombre_cliente=models.CharField(max_length=30)
    apellido_cliente=models.CharField(max_length=30)
    telefono_cliente=models.CharField(max_length=10)
    direccion_cliente=models.CharField(max_length=50)
    cuenta=models.ForeignKey(Cuenta, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.nombre_cliente, self.apellido_cliente)   
    
    def save(self):
        self.nombre_cliente=self.nombre_cliente.upper()
        super(Cliente, self).save()
        
    class Meta:
        verbose_name_plural="Clientes"