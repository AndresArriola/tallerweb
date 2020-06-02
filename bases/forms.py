from django.forms import *
from .models import Reserva2,Empleado,Servicio


class Reservaform(ModelForm):
    class Meta:
        model=Reserva2
        fields= {'nombre','apellido','correo','fecha_reserva' ,'marca','modelo','servicio','especialista'}
        labels = { 'nombre': 'Nombre','apellido': 'Apellido','correo': 'Correo','fecha_reserva': 'Fecha' ,
        'marca': 'Marca','modelo': 'Modelo',
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