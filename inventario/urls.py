from django.urls import path
from . import views
from .views import ProductoListView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('', views.inicio, name='inicio'),
    path('producto/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('categoria/crear/ajax/', views.crear_categoria_ajax, name='crear_categoria_ajax'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),

    #Vista genérica
    path('productos/', ProductoListView.as_view(), name='productos_generica'),
]
