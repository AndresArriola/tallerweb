from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from .models import Servicio, Empleado, Reserva2
from django.urls import reverse_lazy
from django import forms

from bases.forms import Reservaform

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django.http import HttpResponseRedirect


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'


    def get_context_data(self, *args, **kwargs):
            reserva = Reserva2.objects.all()
            servicio = Servicio.objects.all()
            empleado = Empleado.objects.all()
            return {'objresv': reserva,'objserv': servicio, 'objempl': empleado}


class Registrar(LoginRequiredMixin,generic.CreateView):
    template_name = 'bases/listo.html'
    login_url='bases:login'
    model = Reserva2
    form_class = Reservaform
    success_message = 'Reserva Creada Correctamente !'
    success_url = reverse_lazy('bases:home')

class Listar(LoginRequiredMixin,generic.TemplateView):
    template_name = 'bases/listar.html'
    login_url='bases:login'

    def get_context_data(self, *args, **kwargs):
            reserva = Reserva2.objects.all()
            servicio = Servicio.objects.all()
            empleado = Empleado.objects.all()
            return {'objresv': reserva,'objserv': servicio, 'objempl': empleado}
