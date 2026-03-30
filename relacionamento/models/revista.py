from .base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Revista(BaseModel):
    nome = models.CharField(max_length=100,
                            help_text= ("Nome da Revista"))
    edicao = models.CharField(max_length=100,
                              help_text= ("Edição(numérico) da Revista"),
                              verbose_name= ("Edição da revista"))

    def __str__(self):
        return self.nome

    def clean(self):
        try:
            existente = Revista.objects.filter(nome__iexact=self.nome).filter(edicao=self.edicao)
            if len(existente) > 0:
                raise ValidationError('Esta edição desta revista já existe')
        except ValueError:
            pass