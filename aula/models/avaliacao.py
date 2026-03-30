from django.db import models
from .base_model import BaseModel


class Avaliacao(BaseModel):
    titulo = models.CharField(max_length=100,
                              verbose_name='Título',
                              help_text='Informe o título para a avaliação')
    data_avaliacao = models.DateField(auto_now=False,
                                      auto_now_add=False)
    data_visita = models.DateField(auto_now=False,
                                   auto_now_add=False)
    comentario = models.TextField(verbose_name="Comentário",
                                  help_text="Escreva seu comentário")
    nota = models.IntegerField(default=0.0,
                               help_text="Digite uma nota de 0 a 5")
    acompanhantes = models.CharField(max_length=20,
                                     help_text="Digite entre: familia, amigos, romantico, a sos")
    likes = models.IntegerField()

    def __str__(self):
        return self.titulo

