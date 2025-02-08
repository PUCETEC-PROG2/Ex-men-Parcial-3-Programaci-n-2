from django import forms
from .models import Artista, Álbum

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'

        
class ÁlbumForm(forms.ModelForm):
    class Meta:
        model = Álbum
        fields = '__all__'
        labels = {
            'Anio de lanzamiento' : 'Año de lanzamiento',
        }
        witgets = {
            'Anio de lanzamiento' : forms.DateInput(attrs={'class': 'form-control'}),
        }