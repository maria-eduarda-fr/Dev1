from django.db import models
from django.utils.translation import gettext_lazy as _

class StatusModeracao(models.TextChoices):
    EXCLUIDA = "excluida", _("Excluída")