from django.conf import settings
from django.db import models
from django.utils import timezone



# Create your models here.
class Postagens(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
class Comentario(models.Model):
    postagem = models.ForeignKey(Postagens, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comentario de {self.autor} na {self.postagem}'