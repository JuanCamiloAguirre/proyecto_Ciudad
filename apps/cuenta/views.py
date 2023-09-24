from django.shortcuts import render
from django.http import HttpResponse
from apps.cuenta.models import Cuenta
from apps.cuenta.form import CuentaForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json
import datetime

# Create your views here.

def index(request):
    return render(request, "cuenta/index.html")

class CuentaList(LoginRequiredMixin, generic.ListView):
    model=Cuenta
    template_name='cuenta/cuenta_list.html'
    context_object_name="obj"
    login_url="login"

class CuentaCreate(LoginRequiredMixin, generic.CreateView):
    model=Cuenta
    template_name='cuenta/cuenta_form.html'
    context_object_name="obj"
    form_class= CuentaForm
    success_url= reverse_lazy('cuenta_listar')
    login_url="login"

    ## Ni idea
    # def form_valid(self, form):
    #     form.instance.tipocuenta=self.request.user
    #     return super().form_valid(form)


class CuentaEdit(LoginRequiredMixin, generic.UpdateView):
    model=Cuenta
    template_name='cuenta/cuenta_form.html'
    context_object_name="obj"
    form_class= CuentaForm
    success_url= reverse_lazy('cuenta_listar')
    login_url="login"

    ## Ni idea x2
    # def form_valid(self, form):
    #     form.instance.nombre_cuenta=self.request.user.id
    #     return super().form_valid(form)

class CuentaDelete(LoginRequiredMixin, generic.DeleteView):
    model=Cuenta
    template_name='cuenta/cuenta_delete.html'
    success_url= reverse_lazy('cuenta_listar')
    context_object_name="obj"

