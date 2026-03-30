from django.db.models import QuerySet
from relacionamento.managers.base_manager import BaseManager
from datetime import date

class PaperManager(BaseManager):
    def future_publications(self) -> list['Paper']:
        today = date.today()
        consulta = self.filter(nome__gt=today)
        return list(consulta)
