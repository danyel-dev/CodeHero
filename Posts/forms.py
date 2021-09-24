from django import forms

from .models import Comentario


class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ('titulo', 'comentario')

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'title_comment', 
                'placeholder': 'Informe um titulo pro comentario'
            }),
            
            'comentario': forms.Textarea(attrs={
                'placeholder': 'Digite seu comentario aqui',
                'class': 'comment_textarea',
                'cols': 50, 'rows': 5
            }),
        }
