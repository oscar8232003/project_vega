from django import forms
from vendedor.models import Productos
from .models import Listas, Productos_listas

class FormCategoria(forms.ModelForm):

    class Meta:

        model = Productos

        fields = [
            'categoria',
        ]

        labels = {
            'categoria': 'Categoria',
        }

        widgets = {
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }

class FormTienda(forms.ModelForm):

    class Meta:

        model = Listas

        fields = [
            'local',
        ]

        labels = {
            'local': 'Locales',
        }

        widgets = {
            'local':forms.Select(attrs = {'class':'form-control'}),
        }

class FormListas(forms.ModelForm):
    class Meta:
        model = Listas

        fields = [
            'user',
            'local',
            'nombre',
            'comentario_cliente',
        ]

        labels = {
            'local':'Local',
            'nombre':'Nombre de la lista',
            'comentario_cliente':'Comentarios',
        }

        widgets = {
            'user':forms.HiddenInput,
            'local':forms.Select(attrs = {'class':'form-control'}),
            'nombre':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Ingrese el nombre de la lista'}),
            'comentario_cliente': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
        }

class Productos_listas_form(forms.ModelForm):
    class Meta:
        model=Productos_listas

        fields=[
            'user',
            'productos',
            'local',
            'lista',
            'cantidad',
            'comentarios',
            'precio_producto',
        ]

        widgets = {
            'user':forms.HiddenInput,
            'productos':forms.HiddenInput,
            'local':forms.HiddenInput,
            'lista':forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control',}),
            'comentarios':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'precio_producto':forms.HiddenInput,
        }