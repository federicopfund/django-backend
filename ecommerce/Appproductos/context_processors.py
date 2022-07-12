
from .models import Categoria

def listarCategorias(request):

    categorias = Categoria.objects.all()
    
    return {'categorias': categorias}
