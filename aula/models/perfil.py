from django.db import models
from .base_model import BaseModel
from ..enumerations import Genero

class Perfil(BaseModel):
    cidade = models.CharField(max_length=255,
                              help_text="Cidade que reside")
    pais = models.CharField(verbose_name="País",
                            max_length=60,
                            help_text="Pais que reside")
    bio = models.CharField(verbose_name="Biografia",
                           max_length=255,
                           help_text="Biografia sobre você para o seu perfil")
    passaporte = models.CharField(verbose_name="Número do passaporte",
                                  max_length=10,
                                  help_text="Digite o número do seu passaporte")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento",
                                       help_text="Use o formato: ",
                                       auto_now=False,
                                       auto_now_add=False)
    genero = models.CharField(verbose_name="Gênero",
                              max_length=20,
                              choices=Genero,
                              default=Genero.NAO_ESPECIFICADO)
    def __str__(self):
        return self.genero