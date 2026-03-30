from .base_model import BaseModel
from django.db import models


class Atividade(BaseModel):
    nome = models.CharField(max_length=100)
    informacoes = models.TextField()
    endereco = models.CharField(max_length=200)
    turno = models.CharField(max_length=8,
                             null=True,
                             blank=True,
                             help_text="Digite manhã, tarde ou noite")  # campo opicional
    duracao = models.TimeField(verbose_name="Duração da atividade",
                               null=True,
                               blank=True,
                               help_text="Duração média da atividade\nUse este formato: HH:MM")
    ingresso = models.BooleanField(help_text="Marque se houver ingresso pago")
    valor = models.DecimalField(default=0.00,
                                max_digits=10,
                                decimal_places=2,
                                verbose_name="Preço",
                                help_text="Digite o valor da atração em R$")
    guia = models.BooleanField(help_text="Marque se a atividade possuir guia")
    participantes = models.IntegerField(help_text="Digite a quantidade de participantes mínima para a atividade")
    nota = models.FloatField(default=0.0,
                             help_text="Digite uma nota de 0 a 5")

    def __str__(self):
        return f"{self.id} - {self.nome}"
