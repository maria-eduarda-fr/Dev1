from rest_framework import serializers
from ..enumerations import Operacoes

class CalculoSerializer(serializers.Serializer):

    primeiro_termo = serializers.FloatField(required=True)
    segundo_termo = serializers.FloatField(required=True)
    operacao = serializers.ChoiceField(required=True,
                                       choices=Operacoes.choices)
    resultado = serializers.CharField(required=False)

    class Meta:
        fields = ['primeiro_termo', 'segundo_termo', 'operacao']

    def calcular(self):
        primeiro_termo = self.validated_data.get('primeiro_termo')
        segundo_termo = self.validated_data.get('segundo_termo')
        operacao = self.validated_data.get('operacao')

        match operacao:
            case Operacoes.ADDITIONS:
                self.validated_data.update({'resultado': primeiro_termo+segundo_termo})
                self.validated_data.update({'operacao': Operacoes.ADDITIONS.label})

            case Operacoes.SUBTRACTION:
                self.validated_data.update({'resultado': primeiro_termo - segundo_termo})
                self.validated_data.update({'operacao': Operacoes.SUBTRACTION.label})

            case Operacoes.MULTIPLICATION:
                self.validated_data.update({'resultado': primeiro_termo * segundo_termo})
                self.validated_data.update({'operacao': Operacoes.MULTIPLICATION.label})

            case Operacoes.DIVISION:
                self.validated_data.update({'resultado': primeiro_termo / segundo_termo})
                self.validated_data.update({'operacao': Operacoes.DIVISION.label})

            case _:
                raise NotImplementedError('Not Impplemented')
