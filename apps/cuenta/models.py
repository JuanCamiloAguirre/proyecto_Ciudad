from django.db import models
from apps.tipocuenta.models import TipoCuenta
# Create your models here.

class Cuenta(models.Model):
    
    nombre_cuenta=models.CharField(max_length=50)
    fecha_apertura=models.DateField()
    salario=models.CharField(max_length=15)
    tipocuenta=models.OneToOneField(TipoCuenta, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_cuenta)

    def save(self):
        self.nombre_cuenta=self.nombre_cuenta.upper()
        super(Cuenta, self).save()
        
    class Meta:
        verbose_name_plural="Cuentas"
