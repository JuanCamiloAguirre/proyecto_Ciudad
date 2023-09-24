from django.shortcuts import render
from django.http import HttpResponse
from apps.tipocuenta.models import TipoCuenta
from apps.tipocuenta.form import TipoCuentaForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json
import datetime

# Create your views here.

def index(request):
    return render(request, "cuenta/index.html")

class TipoCuentaList(LoginRequiredMixin, generic.ListView):
    model=TipoCuenta
    template_name='tipocuenta/tipo_list.html'
    context_object_name="obj"
    login_url="login"


class TipoCuentaCreate(LoginRequiredMixin, generic.CreateView):
    model=TipoCuenta
    template_name='tipocuenta/tipo_form.html'
    context_object_name="obj"
    form_class= TipoCuentaForm
    success_url= reverse_lazy('tipo_listar')
    login_url="login"


class TipoCuentaEdit(LoginRequiredMixin, generic.UpdateView):
    model=TipoCuenta
    template_name='tipocuenta/tipo_form.html'
    context_object_name="obj"
    form_class= TipoCuentaForm
    success_url= reverse_lazy('tipo_listar')
    login_url="login"

class TipoCuentaDelete(LoginRequiredMixin, generic.DeleteView):
    model=TipoCuenta
    template_name='tipocuenta/tipo_delete.html'
    success_url= reverse_lazy('tipo_listar')
    context_object_name="obj"
