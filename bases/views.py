from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from .models import Servicio, Empleado

from django.http import HttpResponseRedirect


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'

class ListarServicio(generic.ListView):
    template_name = 'bases/registrar.html'
    model = Servicio
    context_object_name = "objserv"    
    ogin_url='bases:login'



class ListarEmpleado(generic.ListView):
    template_name = 'bases/registrar.html'
    model = Empleado
    context_object_name = "objempl"    
    ogin_url='bases:login'

