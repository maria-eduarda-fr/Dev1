from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from datetime import datetime
class SaudacaoView(View):
    @staticmethod
    def get(request):
        agora = datetime.now()
        mensagem = 'boa noite'
        if 12 > agora.hour > 6:
            mensagem = 'bom dia'
        elif 0 < agora.hour <= 6:
            mensagem = 'boa madrugada'
        completo = {
            'mensagem': f'{mensagem}, visitante!',
            'horario': agora,
            'endereco': f'endereço:{request.META["REMOTE_ADDR"]}'
        }
        return render(request, 'primeira.html', completo)
