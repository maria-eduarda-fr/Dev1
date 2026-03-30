from django.urls import path

from .views import *
from .views.reporter import *

app_name = 'services'

urlpatterns = [
    path('', api_root, name='api-root'),
    path('saudacao', saudacao, name='saudacao'),
    path('saudacao/classe', ExemploSaudacao.as_view(), name='saudacao_classe'),
    path('calculo', calculo, name='calculo'),

    path('reporter', ReporterListService.as_view(), name='reporter_list'),
]
