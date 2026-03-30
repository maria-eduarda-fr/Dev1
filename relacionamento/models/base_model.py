from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True  # não gera uma tabela
        app_label = 'relacionamento'  # nome do app        (fica na frente do nome da tabela -> prefixo da tabela)

