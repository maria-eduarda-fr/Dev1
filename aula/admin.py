from django.contrib import admin
from aula.models import Atividade
from aula.models import Avaliacao
from aula.models import Perfil
from aula.models import *
from aula.models import Viagem

# Register your models here.
admin.site.register((Atividade, Perfil, Avaliacao, Viagem))
admin.site.register(Local, LocalAdmin)

