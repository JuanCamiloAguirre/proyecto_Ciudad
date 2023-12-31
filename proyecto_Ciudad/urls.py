"""
URL configuration for proyecto_Ciudad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include, path
from apps.cuenta.views import index
from apps.cliente.views import index
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path('admin/', admin.site.urls),
    re_path(r'^cliente/', include('apps.cliente.urls')),
    re_path(r'^cuenta/', include('apps.cuenta.urls')),
    re_path(r'^tipocuenta/', include('apps.tipocuenta.urls')),
    re_path(r'^usuario/', include('apps.usuario.urls')),
    re_path(r'^ini/', LoginView.as_view(template_name="usuario/index.html"), name="login"),
    re_path(r'^logout/', logout_then_login, name='logout'),
    path('inv/', include(('apps.inv.urls', 'inv'), namespace='inv')),
    path('cmp/', include(('apps.cmp.urls', 'cmp'), namespace='cmp')),
]
