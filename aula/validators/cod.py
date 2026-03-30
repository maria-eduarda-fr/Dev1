from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#decorator utilizado para tornar a classe "serrializavel"
#ou seja, como construir e reconstruir essas classes
@deconstructible
class CodValidator(cod):
    def __init__(self, cod="00000000"):
        self.code = cod

    def __call__(self, valor):
        if valor == self.code:
            raise ValidationError(
                _("Valor inválido"),
                params={'valor': valor},
            )

    def __equal__(self,outro):
        return (
            isinstance(outro, CodValidator)
            and self.code == outro.code
        )

    