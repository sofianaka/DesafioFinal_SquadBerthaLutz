from django import forms
from .models import Postagens, Comentario


class PostForm(forms.ModelForm):
    class Meta:
        model = Postagens
        fields = ["titulo", "conteudo"]

class ComentarioForm(forms.ModelForm):  
    class Meta:
        model = Comentario  
        fields = ["texto"]  