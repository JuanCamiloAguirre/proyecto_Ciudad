from  django.urls import re_path, include
from apps.tipocuenta.views import index, TipoCuentaList, TipoCuentaCreate, TipoCuentaEdit, TipoCuentaDelete

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^nuevo$', TipoCuentaCreate.as_view(), name='tipo_crear'),
    re_path(r'^listar$', TipoCuentaList.as_view(), name='tipo_listar'),
    re_path(r'^editar/(?P<pk>\d+)/$', TipoCuentaEdit.as_view(), name='tipo_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', TipoCuentaDelete.as_view(), name='tipo_eliminar'),
]