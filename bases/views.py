from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from .models import Servicio, Empleado

from django.http import HttpResponseRedirect


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'

    def get_context_data(self, *args, **kwargs):
            servicio = Servicio.objects.all()
            empleado = Empleado.objects.all()
            return {'objserv': servicio, 'objempl': empleado}
   
class Gracias(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/gracias.html'
    login_url='bases:login'


