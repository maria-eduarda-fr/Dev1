from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .base_model import BaseModel
from django.contrib import admin

class Local(BaseModel):
    nome = models.CharField(max_length=100,
                            help_text="Digite o nome do local")
    informacoes = models.TextField(verbose_name="Informações",
                                   help_text="Digite as informações relevântes sobre o local")
    endereco = models.CharField(max_length=200,
                                help_text="Digite: Nome da rua, número, bairro, cidade")
    horario_abertura = models.TimeField(auto_now=False,
                                        auto_now_add=False,
                                        verbose_name="Horário de abertura",
                                        help_text="Use este formato: HH:MM")
    horario_fechamento = models.TimeField(auto_now=False,
                                          auto_now_add=False,
                                          verbose_name="Horário de fechamento",
                                          help_text="Use este formato: HH:MM")
    ingresso = models.BooleanField(help_text="marque se houver ingresso pago")
    valor = models.DecimalField(default=0.0,
                                max_digits=10,
                                decimal_places=2,
                                null=True,
                                blank=True,
                                help_text="Digite o valor do ingresso em R$")
    acessibilidade = models.BooleanField(help_text="")
    classificacao_idade = models.IntegerField(verbose_name="Classificação de idade",
                                              help_text="Digite a idade mínima permitida para o local")
    contato = models.EmailField(max_length=254,
                                help_text="Informe o email de contato do local")
    nota = models.FloatField(default=0.0,
                             help_text="Digite uma nota de 0 a 5",
                             validators=[MinValueValidator(1),
                                         MaxValueValidator(5)])

    def __str__(self):
        return f"{self.nome}"


class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato')  #mostra os atributos da classe como 'titulo"
    #readonly_fields = ()    #não podem ser alterados - são inseridos automaticamente
    search_fields = ('nome',)    #campo de pesquisa
    #list_filter = ()