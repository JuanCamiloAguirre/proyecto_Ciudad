from django.shortcuts import render
from django.http import HttpResponse
from apps.cliente.models import Cliente
from apps.cliente.form import ClienteForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json
import datetime

# Create your views here.

def index(request):
    return render(request, "cuenta/index.html")

class ClienteList(LoginRequiredMixin, generic.ListView):
    model=Cliente
    template_name='cliente/cliente_list.html'
    context_object_name="obj"
    login_url="login"


class ClienteCreate(LoginRequiredMixin, generic.CreateView):
    model=Cliente
    template_name='cliente/cliente_form.html'
    context_object_name="obj"
    form_class= ClienteForm
    success_url= reverse_lazy('cliente_listar')
    login_url="login"

class ClienteEdit(LoginRequiredMixin, generic.UpdateView):
    model=Cliente
    template_name='cliente/cliente_form.html'
    context_object_name="obj"
    form_class= ClienteForm
    success_url= reverse_lazy('cliente_listar')
    login_url="login"

class ClienteDelete(LoginRequiredMixin, generic.DeleteView):
    model=Cliente
    template_name='cliente/cliente_delete.html'
    success_url= reverse_lazy('cliente_listar')
    context_object_name="obj"