from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def valida_par(valor):
    try:
        if int(valor) % 2 != 0:
            raise ValidationError(
                _("Não é um valor par"),
                params={'valor': valor}#campo que está validando,
            )
    except ValueError:
        pass

