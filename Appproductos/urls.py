from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import ProductoDetailView, ProductoNew, ProductoEdit, ProductoDel


urlpatterns = [

    path('', views.productos, name='Productos'),
    path('categoria/<int:categoria_id>/', views.categoria, name='Categoria'),
    path('buscar/', views.buscar, name='Buscar'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='Producto_detalle'),

    path('producto/new',ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>',ProductoEdit.as_view(), name='producto_edit'),
    path('producto/delete/<int:pk>',ProductoDel.as_view(), name='producto_del'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)