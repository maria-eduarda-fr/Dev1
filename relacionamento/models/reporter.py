from .base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from relacionamento.validators import valida_cpf
from ..managers.reporter_manager import ReporterManager


class Reporter(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            verbose_name=_('Reporter'),
                            help_text=_('Nome do reporter'))
    cpf = models.CharField(max_length=11,
                           validators=[MinLengthValidator(11),valida_cpf],
                           verbose_name=_('CPF'),
                           help_text=_('Insira o CPF sem pontos'))
    email = models.EmailField(max_length=254,)

    objects = ReporterManager()

    class Meta:
        permissions = [
            ('generate_name_reporter', 'Can generate name')
        ]

    def __str__(self):
        return self.nome

    def clean(self):
        try:
            if "pedro" in self.nome.lower():
                raise ValidationError(
                    _("Não pode conter o nome pedro")
                )
        except ValueError:
            pass