from django import forms
from vendedor.models import Productos

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
