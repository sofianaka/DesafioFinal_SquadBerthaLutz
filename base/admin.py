from django.contrib import admin
from .models import Postagens


# Register your models here.
class PostagensAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao', 'data_publicacao')
    list_filter = ('data_criacao', 'autor')
    search_fields = ('titulo', 'conteudo')

admin.site.register(Postagens, PostagensAdmin)