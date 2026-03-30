from django.db import models
from .base_model import BaseModel
from ..enumerations import Transporte

class Viagem(BaseModel):
    transporte = models.CharField(max_length=50,
                                  choices=Transporte,
                                  default=Transporte.OUTRO,
                                  help_text="Selecione o tipo de transporte que você usará até o destino da viagem")