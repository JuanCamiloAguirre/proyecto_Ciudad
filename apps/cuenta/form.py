from django import forms
from apps.cuenta.models import Cuenta

class CuentaForm (forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [
            'nombre_cuenta',
            'fecha_apertura',
            'salario',
            'tipocuenta',
      
        ]
        labels ={
            'nombre_cuenta': 'Nombre de la Cuenta',
            'fecha_apertura': 'Fecha de Apertura',
            'salario': 'Salario',
            'tipocuenta': 'Tipo de Cuenta',

        }
        Widgets={
            'nombre_cuenta': forms.TextInput,
            'fecha_apertura': forms.DateTimeField,
            'salario': forms.TextInput,
            'tipocuenta': forms.Select

        }
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
