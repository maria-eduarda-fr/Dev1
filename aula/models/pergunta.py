from django.db import models
from .base_model import BaseModel
from ..enumerations import StatusModeracao


class Pergunta(BaseModel):
    pergunta = models.CharField(max_length=255)
    status_moderacao = models.CharField(max_length= 40,
                                        verbose_name="Status de moderação",
                                        choices=StatusModeracao,
                                        default=StatusModeracao.EXCLUIDA)
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.pergunta