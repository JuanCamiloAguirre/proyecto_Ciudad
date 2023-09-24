from  django.urls import re_path, include
from apps.cuenta.views import index, CuentaList, CuentaCreate, CuentaEdit, CuentaDelete

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^nuevo$', CuentaCreate.as_view(), name='cuenta_crear'),
    re_path(r'^listar$', CuentaList.as_view(), name='cuenta_listar'),
    re_path(r'^editar/(?P<pk>\d+)/$', CuentaEdit.as_view(), name='cuenta_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', CuentaDelete.as_view(), name='cuenta_eliminar'),
]