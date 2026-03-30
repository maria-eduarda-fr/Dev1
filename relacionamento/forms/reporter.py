from .base_form import BaseForm
from ..models import Reporter


class ReporterForm(BaseForm):
    class Meta:
        model = Reporter
        fields = '__all__' #objeto iteravel/lista com o nome dos atributos
                           # entre aspas dos campos que quer no form
