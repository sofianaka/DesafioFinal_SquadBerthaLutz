from django.db import models


# Create your models here.
class Postagens(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=50)
