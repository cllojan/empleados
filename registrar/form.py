from django import forms 
from .models import Empleado


class EmpleadosForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('nombre_comp','codigo_emp','celular','posicion')
        labels ={
            'nombre_comp':'Nombre Completo',
            'codigo_emp':'Codigo Empleado'
        }
    def __init__(self,*args, **kwargs):
        super(EmpleadosForm,self).__init__(*args,**kwargs)
        self.fields['posicion'].empty_label = 'Seleccionar'
        self.fields['codigo_emp'].required = False