from django.forms import *
from .models import Reserva2,Empleado,Servicio


class Reservaform(ModelForm):
    class Meta:
        model=Reserva2
        fields= {'fecha_reserva' ,'nombre','apellido','marca','modelo','correo','servicio','especialista'}
        labels = { 'fecha_reserva': 'Fecha' ,'nombre': 'Nombre',
        'apellido': 'Apellido','marca': 'Marca','modelo': 'Modelo','correo': 'Correo',
        'servicio': 'Servicio','especialista': 'Especialista'
        }
        widget={ 'fecha_reserva': DateTimeInput ,'nombre': TextInput,
        'apellido': TextInput,'marca': TextInput,'modelo': TextInput,'correo': TextInput,'servicio': TextInput,'especialista': TextInput,
        }

class EspecialistaForm(ModelForm):
     class Meta:
         model=Empleado
         fields= ['p_nombre_empleado']


#class Reservaform2(ModelForm):
 #       form_classes = {
  #      'reserva': Reservaform2,
  #      'empleado': EspecialistaForm,
  #  }