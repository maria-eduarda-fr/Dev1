from django.db.models import QuerySet
from relacionamento.managers.base_manager import BaseManager


class ReporterManager(BaseManager):
    def find_by_name(self, nome: str):
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(nome__icontains=nome).order_by('nome')
            return consulta
        else:
            raise TypeError('O nome deve ser string e não pode ser vazio')


