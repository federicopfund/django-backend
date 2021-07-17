

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy



from .models import Producto, Categoria
from .forms import ProductoForm

def productos(request):
 
    productos = Producto.objects.all()

    return render(request,'productos/productos.html',{'productos': productos[:3], 'resto_productos':productos[3:10]})


def categoria(request, categoria_id):

    productos = Producto.objects.filter(categorias_id=categoria_id)

    return render(request,'productos/categoria.html',{'productos': productos})




def buscar(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(categorias__nombre__icontains=query)
        )
        results = Producto.objects.filter(qset).distinct()
    else:
        results = []
    return render(request,'productos/buscar.html', {'results': results,'query': query})    



class ProductoDetailView(DetailView):

    model = Producto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Producto.objects.all()

        return context


class ProductoNew(CreateView):
    model = Producto
    template_name = "productos/producto_form.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("Productos")



    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()

        return context


class ProductoEdit(UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("Productos")



    def form_valid(self, form):
        return super().form_valid(form)

class ProductoDel(DeleteView):
    model = Producto
    template_name = 'productos/producto_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("Productos")
