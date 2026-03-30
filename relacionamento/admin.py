from django.contrib import admin
from relacionamento.models import Pessoa, Reporter, Revista, Artigo, Paper, Publicacao

# Register your models here.

admin.site.register((Pessoa, Reporter, Revista,Artigo, Paper, Publicacao))