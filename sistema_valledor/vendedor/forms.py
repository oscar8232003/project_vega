from django import forms
from .models import Productos, Local, Oferta
#from cliente.models import Productos_listas

class Productos_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'user',
            'nombre',
            'precio',
            'categoria',
            'oferta',
            'precio_oferta',
            'stock',
            'imagen',
            'unidad_medida',
            'comentario',
            'activado',
        ]

        labels = {
            'nombre':'Nombre',
            'precio':'Precio',
            'categoria':'Categoria del producto',
            'oferta':'Esta en oferta en producto?',
            'precio_oferta':'Precio de la oferta',
            'stock':'Stock',
            'imagen':'Imagen del producto',
            'unidad_medida':'Unidad de medida para el producto',
            'comentario':'Comentarios sobre el producto',
            'activado':'El producto va a estar activado?',
        }

        widgets = {
            'user': forms.HiddenInput(),
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el nombre del producto'}),
            'precio':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese el precio'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'oferta':forms.CheckboxInput(attrs={'style':'width:18px; height:18px'}),
            'precio_oferta':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese el precio de la oferta'}),
            'stock':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese el nombre del producto'}),
            'imagen':forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'unidad_medida':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione la unidad de medida'}),
            'comentario':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion del producto', 'rows':3}),
            'activado': forms.CheckboxInput(attrs={'style':'width:18px; height:18px'}),
        }

class Local_form(forms.ModelForm):
    class Meta:
        model = Local

        fields = [
            'user',
            'nombre_local',
            'ubicacion_local',
            'imagen_muestra',
            'imagen_banner',
            'activado'
        ]

        label = {
            'nombre_local':"Nombre del local",
            'ubicacion_local':"Ubicacion del local",
            'imagen_muestra':"Imagen de muestra pequeña",
            'imagen_banner':"Imagen superior",
            'activado': "El local estara activo?"
        }

        widgets = {
            'user':forms.HiddenInput,
            'nombre_local':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Ingrese el nombre '}),
            'ubicacion_local':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Ingrese la ubicacion'}),
            'imagen_muestra':forms.ClearableFileInput,
            'imagen_banner':forms.ClearableFileInput,
            'activado': forms.CheckboxInput(attrs={'style': 'width:18px; height:18px'}),
        }

class Ofertas_form(forms.ModelForm):
    class Meta:
        model=Oferta

        fields=[
            'local',
            'oferta',
            'tipo_oferta',
            'activado',
        ]

        widgets = {
            'local':forms.HiddenInput,
            'oferta':forms.TextInput(attrs={'placeholder':'Ingrese la oferta a mostrar','class':'form-control'}),
            'tipo_oferta':forms.Select(attrs={'class':'form-control'}),
            'activado':forms.CheckboxInput(attrs={'style': 'width:18px; height:18px'}),
        }
