from django import forms
from apps.tipocuenta.models import TipoCuenta

class TipoCuentaForm (forms.ModelForm):
    class Meta:
        model = TipoCuenta
        fields = [
            'descripcion',
        ]
        labels ={
            'descripcion': 'Descripcion',
        }
        Widgets={
            'descripcion': forms.TextInput
        }
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        

    
