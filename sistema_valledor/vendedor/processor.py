from .models import Categoria_Productos

def Traer_Categorias(request):
    categorias = Categoria_Productos.objects.all()
    return {'Categorias': categorias}
