from django.db import models
from django.utils.translation import gettext_lazy as _

class Genero(models.TextChoices):
    MASCULINO = "masculino", _("Masculino")
    FEMININO = "feminino", _("Feminino")
    OUTRO = "outro", _("Outro")
    NAO_ESPECIFICADO = "nao especificado", _("Não especificado")

