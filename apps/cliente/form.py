from django import forms
from apps.cliente.models import Cliente

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'cedula',
            'nombre_cliente',
            'apellido_cliente',
            'telefono_cliente',
            'direccion_cliente',
            'cuenta',

        ]
        labels ={
            'cedula':'Cedula',
            'nombre_cliente': 'Nombre',
            'apellido_cliente': 'Apellido',
            'telefono_cliente': 'Telefono',
            'direccion_cliente': 'Dirección',
            'cuenta':'Cuenta',

        }
        Widgets={
            'cedula': forms.TextInput,
            'nombre_cliente': forms.TextInput,
            'apellido_cliente': forms.TextInput,
            'Telefono_cliente': forms.TextInput,
            'direccion_cliente': forms.TextInput,
            'cuenta': forms.Select
        }
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
