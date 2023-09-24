from django.urls import include, path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel,\
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, \
        MarcaView, MarcaNew, MarcaEdit, marca_inactivar, \
        UnidadMedidaView, UnidadMedidaNew,  UnidadMedidaEdit, unidadmedida_inactivar, \
            ProductoView,  ProductoNew, ProductoEdit, Producto_inactivar
        # MarcaDel


urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'categorias/', CategoriaView.as_view(), name='categoria_list'),
    path(r'categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path(r'categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path(r'categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),
    
    path(r'subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path(r'subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path(r'subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path(r'subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_del'),
    
    path(r'marcas/', MarcaView.as_view(), name='marca_list'),
    path(r'marcas/new', MarcaNew.as_view(), name='marca_new'),
    path(r'marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    # path(r'marcas/delete/<int:pk>', MarcaDel.as_view(), name='marca_del'),
    path(r'marcas/inactivar/<int:id>', marca_inactivar, name='marca_inactivar'),
    
    path(r'unidadmedidas/', UnidadMedidaView.as_view(), name='unidadmedida_list'),
    path(r'unidadmedidas/new', UnidadMedidaNew.as_view(), name='unidadmedida_new'),
    path(r'unidadmedidas/edit/<int:pk>', UnidadMedidaEdit.as_view(), name='unidadmedida_edit'),
    path(r'unidadmedidas/inactivar/<int:id>', unidadmedida_inactivar, name='unidadmedida_inactivar'),
    
    path(r'productos/', ProductoView.as_view(), name='producto_list'),
    path(r'productos/new', ProductoNew.as_view(), name='producto_new'),
    path(r'productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path(r'productos/inactivar/<int:id>', Producto_inactivar, name='producto_inactivar'),
]
