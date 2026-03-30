from django.db import models
from django.utils.translation import gettext_lazy as _

class Transporte(models.TextChoices):
    CARRO = "carro", _("Carro")
    MOTO = "motocicleta", _("Motocicleta")
    ONIBUS = "onibus", _("Ônibus")
    TREM = "trem", _("Trem")
    METRO = "metro", _("Metrô")
    AVIAO = "aviao", _("Avião")
    BARCO = "barco", _("Barco")
    CAMINHANDO = "caminhando", _("Caminhando")
    BICICLETA = "bicicleta", _("Bicicleta")
    OUTRO = "outro", _("Outro")