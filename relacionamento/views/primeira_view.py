from django.shortcuts import render, redirect, HttpResponse
from django.views import View


class PrimeiraView(View):
    @staticmethod
    def get(request):
        mens = {'mensagem': 'Bom dia Dev1'}
        return render(request, 'primeira.html', mens)