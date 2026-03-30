from .base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from relacionamento.validators import valida_cpf
from datetime import date

class Pessoa(BaseModel):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nascimento = models.DateField(verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=11,
                           verbose_name="CPF",
                           validators=[MinLengthValidator(11),valida_cpf])

    def __str__(self):
        return f'{self.nome}'

    def clean(self):
        hoje = date.today()

        try:
            if self.nascimento > hoje.replace(year=hoje.year - 18):
                raise ValidationError(
                    _("Você precisa ter 18 anos.")
                )
        except ValueError:
            pass