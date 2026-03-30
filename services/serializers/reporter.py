from rest_framework import serializers
from relacionamento.models import Reporter
#from services.serializers

class ReporterMinimalSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField()

    class Meta:
        model = Reporter
        fields = ['nome', 'cpf', 'email'] #campos do model que queremos que mostrar

    def create(self, validated_data):
        #permite criar um objeto
        return Reporter.objects.create(**validated_data)

