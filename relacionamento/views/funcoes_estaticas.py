from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from datetime import datetime
from django.core import serializers
from relacionamento.models import Reporter


def primeira_view(request):
    contexto = {
        'mensagem': 'Bom dia Dev1'
    }
    return render(request, 'primeira.html', contexto)


def saudacao(request):
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


def nome(request, name):
    exemplo = Reporter.objects.find_by_name(name)
    objeto = serializers.serialize('python', exemplo)
    return JsonResponse(objeto, safe=False)


def exercicio(request, palavra):
    '''Codificação:
    valores em maiuscula ou minuscuscula
    A = 4
    E = 3
    I = 1
    O = 0
    U = v'''
    palavra_inicial = palavra.strip().lower()

    palavra_codificada = palavra_inicial.replace('a', '4')
    palavra_codificada = palavra_codificada.replace('e', '3')
    palavra_codificada = palavra_codificada.replace('i', '1')
    palavra_codificada = palavra_codificada.replace('o', '0')
    palavra_codificada = palavra_codificada.replace('u', 'v')
    mensagem = (f'<html><body><h3>palavra inicial:{palavra}<br/>palavra codificada:{palavra_codificada}</h3>'
                f'</body></htlm>')
    return HttpResponse(mensagem)


def calculo(request, valor_x, valor_y):
    try:
        divisao = valor_x / valor_y
    except ZeroDivisionError:
        divisao = 'Não é possível fazer divisão por 0'
    mensagem = (f'<html><body><h2>Valor 1: {valor_x}  Valor 2: {valor_y}</h2>'
                f'<h3>Soma: {valor_x + valor_y}<br/>'
                f'Subtração: {valor_x - valor_y}<br/>'
                f'Multiplicação: {valor_x * valor_y}<br/>'
                f'Divisão: {divisao}</h3>'
                f'</body></htlm>')
    return HttpResponse(mensagem)


def calculo_especifico(request, valor_x, valor_y, operador):
    if operador == '+':
        calculo = f'{valor_x} + {valor_y} = {valor_x + valor_y}'
    elif operador == '-':
        calculo = f'{valor_x} - {valor_y} = {valor_x - valor_y}'
    mensagem = (f'<html><body><h2>{calculo}</h2>'
                f'</body></htlm>')
    return HttpResponse(mensagem)
