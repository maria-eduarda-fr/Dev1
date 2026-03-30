from .base_model import BaseModel
from django.db import models
from . import Reporter, Revista
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from datetime import date
from ..managers.paper_manager import PaperManager

class Paper(BaseModel):
    titulo = models.CharField(max_length=200,
                              validators=[MinLengthValidator(5)],
                              verbose_name=_('Título'),
                              help_text="Insira o título do artigo.")
    data_publicacao = models.DateField(verbose_name=_('Data publicação'))
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    revistas = models.ManyToManyField(Revista,
                                      null=True,blank=True,
                                      through='Publicacao',
                                      through_fields=("paper", "revista"))

    objects = PaperManager()

    def __str__(self):
        return f"{self.titulo} por {self.reporter.nome}"

    def clean(self):
        hoje = date.today()
        try:
            if self.data_publicacao < hoje:
                raise ValidationError(
                    _("A data de publicação não pode ser anterior a hoje")
                )
        except ValueError:
            pass
