from django.urls import include, path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, ProveedorInactivar,\
    ComprasView, compras, CompraDetDelete

from .reportes import reporte_compras, imprimir_compra

urlpatterns = [
    path(r'proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path(r'proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path(r'proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path(r'proveedores/inactivar/<int:id>', ProveedorInactivar, name='proveedor_inactivar'),
    
    path(r'compras/', ComprasView.as_view(), name='compras_list'),
    path(r'compras/new', compras, name='compras_new'),
    path(r'compras/edit/<int:compra_id>', compras, name='compras_edit'),
    path(r'compras/<int:compra_id>/delete/<int:pk>', CompraDetDelete.as_view(), name='compras_del'),
    
    path(r'compras/listado', reporte_compras, name='compras_print_all'),
    path(r'compras/<int:compra_id>/imprimir', imprimir_compra, name='compras_print_one'),
    
]
