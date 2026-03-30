from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from relacionamento.models import Reporter
from django.http import JsonResponse
from django.core import serializers


class NomeView(View):
    @staticmethod
    def get(request, nome=''):
        if nome == '' or nome == ' ':
            dados = list(Reporter.objects.all())
        else:
            dados = Reporter.objects.find_by_name(nome)

        mensagem = ''
        tipo = str(request.GET.get('type'))
        match tipo.lower():
            case 'http':
                for objeto in dados:
                    mensagem += (f'<b>ID:</b> {objeto.id}<br/>'
                                 f'<b>Nome:</b> {objeto.nome}<br/>'
                                 f'<b>CPF:</b> {objeto.cpf}<br/>'
                                 f'<b>Paper:</b> {objeto.email}<br/>'
                                 f'<hr/>')
                return HttpResponse(mensagem, status=200)
            case 'json':
                objetos = serializers.serialize('python', dados)
                return JsonResponse(objetos, safe=False)
            case _:
                mensagem += 'Bad request'
                return HttpResponse(mensagem, status=400)
