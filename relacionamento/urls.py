from django.urls import path
from relacionamento.views import  funcoes_estaticas as views_funcoes
from relacionamento.views.nome_view import NomeView
from relacionamento.views.primeira_view import PrimeiraView
from relacionamento.views.saudacao_view import SaudacaoView
from relacionamento.views.reporter_classe import *
from relacionamento.views.reporter_generic import *
import relacionamento.views.reporter as views_reporter


app_name = 'relacionamento'
urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name='primeira_view'),
    path('funcao/saudacao', views_funcoes.saudacao, name='saudacao'),
    path('funcao/exercicio/<str:palavra>', views_funcoes.exercicio, name='func_exercicio'),
    path('funcao/exercicio/calculo/<int:valor_x>/<int:valor_y>', views_funcoes.calculo, name='calculos'),
    path('funcao/exercicio/calculo/<int:valor_x>/<int:valor_y>/<str:operador>', views_funcoes.calculo_especifico, name='calculo'),
    path('funcao/reporter', views_reporter.reporter_list, name='reporter'),
    path('funcao/reporter/read/<int:pk>', views_reporter.reporter_detail, name='reporter_detail' ),
    path('funcao/reporter/delete/<int:pk>', views_reporter.reporter_delete, name='reporter_delete'),
    path('funcao/reporter/create', views_reporter.reporter_create, name='reporter_create'),
    path('funcao/reporter/update/<int:pk>', views_reporter.reporter_update, name='reporter_update'),
    path('funcao/reporter/generate_name/<int:pk>', views_reporter.reporter_generate_name, name='reporter_generate_name'),

    path('generic/reporter', ReporterListGeneric.as_view(), name='generic_reporter'),
    path('generic/reporter/read/<int:pk>', ReporterDetailGeneric.as_view(), name='generic_reporter_detail'),
    path('generic/reporter/delete/<int:pk>', ReporterDeleteGeneric.as_view(), name='generic_reporter_delete'),
    path('generic/reporter/update/<int:pk>', ReporterUpdateGeneric.as_view(), name='generic_reporter_update'),
    path('generic/reporter/create', ReporterCreateGeneric.as_view(), name='generic_reporter_create'),

    path('classe/reporter', ReporterListView.as_view(), name='classe_reporter'),
    path('classe/reporter/read/<int:pk>', ReporterDetailView.as_view(), name='classe_reporter_detail'),
    path('classe/reporter/delete/<int:pk>', ReporterDeleteView.as_view(), name='classe_reporter_delete'),
    path('classe/reporter/create', ReporterCreateView.as_view(), name='classe_reporter_create'),
    path('classe/reporter/update/<int:pk>', ReporterUpdateView.as_view(), name='classe_reporter_update'),
    path('classe/reporter/generate_name/<int:pk>', ReporterGenerateNameView.as_view(), name='classe_reporter_generate_name'),
    path('classe/<str:name>', views_funcoes.nome, name='nome'),
    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe'),
    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_view_classe'),
    path('classe/<str:nome>', NomeView.as_view(), name='nome_view'),
]