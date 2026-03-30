from django.db import models
from relacionamento.models import BaseModel, Revista, Pessoa, Paper


class Publicacao(BaseModel):
    revista = models.ForeignKey(Revista, on_delete=models.RESTRICT)
    paper = models.ForeignKey(Paper, on_delete=models.RESTRICT)
    editor = models.ForeignKey(Pessoa, on_delete=models.RESTRICT)
    data = models.DateField()
    observacao = models.TextField()

    def __str__(self):
        ano, mes, dia = str(self.data).split('-')
        return f'{self.revista}: {self.paper} editado por {self.editor} em {dia}/{mes}/{ano}'