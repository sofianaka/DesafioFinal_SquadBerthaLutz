from django import forms
from .models import Postagens


class PostForm(forms.ModelForm):
    class Meta:
        model = Postagens
        fields = ["titulo", "conteudo"]