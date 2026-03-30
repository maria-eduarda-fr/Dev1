from manage import *
import contextlib, io

saida = io.StringIO()

#inicialização do django
with contextlib.redirect_stdout(saida):
    main()

#para criar superuser
from django.contrib.auth import get_user_model
#imports dos models
from relacionamento.models import Revista, Reporter, Paper, Publicacao
from datetime import date

#superuser
#User = get_user_model()
#User.objects.create_superuser('<user>', '<EMAIL>', '<password>')


def create_basic_relacionamentos():
    '''Criação basica de objetos dos models: Revista, Reporter, Paper.'''

    revista1 = Revista(nome='Revista anual de esportes', edicao= 5)
    revista1.full_clean()
    revista1.save()
    print('revista criada')

    reporter1 = Reporter(nome='Lucas da Silva Oliveira', cpf='84079070306', email='lucas@gmail.com')
    reporter1.full_clean()
    reporter1.save()


    paper1 = Paper(titulo='A vista original do Alabama', data_publicacao=date(2025,10,15), reporter=reporter1)
    paper1.full_clean()
    paper1.save()

def read_publications():
    publicacoes = Publicacao.objects.all()
    for publicacao in publicacoes:
        print(publicacao.revista, publicacao.data)

def insert_revista():
    nome = input('Digite o nome da revista: ').strip().title()
    edicao = int(input(f'Digite a edicao da revista {nome}: '))

    revista = Revista(nome=nome, edicao=edicao)
    revista.full_clean()
    revista.save()
    print('revista criada com sucesso')

def find_revista():
    flag = True
    while flag:
        menu = int(input('Digite a busca que você deseja:\n'
                         '1 - Busca por nome de revista\n'
                         '2 - Busca por edicao\n'))
        if menu == 1 or menu == 2:
            flag = False

    if menu == 1:
        nome = input('Digite o nome da revista: ').strip()
        query = Revista.objects.filter(nome__icontains=nome)
        if len(query) > 0:
            for revista in query:
                print(f'{revista.nome} - edição: {revista.edicao}')
    elif menu == 2:
        edicao = int(input('Digite a edição para uma revista: '))
        query = Revista.objects.filter(edicao=edicao)
        print(f'REVISTAS NA EDIÇÃO {edicao}')
        for revista in query:
            print(f'{revista.nome}')



'''
def emitir_relatorio():
    consulta_nome = Estatistica.objects.all().order_by("atleta__nome").order_by("evento__data")
    print('ESTATÍSTICAS')
    for i in consulta_nome:
        print(f'nome atleta: {i.atleta.nome}\n'
              f'evento: {i.evento.nome}\n'
              f'data: {i.evento.data}\n'
              f'pontuação/colocação: {i.pontuacao}\n')
'''


"""
def menu():

    menu_aberto = True

    while menu_aberto:
        print('0 - Sair\n'
              '1 - popular banco\n'
              '2 - cria user admin com senha admin\n'
              '3 - buscar_corredores_vencedores()\n'
              '4 - buscar_maiores_pontuadores_eventos_oficiais()\n'
              '5 - buscar_participantes()\n'
              '6 - buscar_evento_participantes_estrangeiros()')

        opcao = input('Selecione uma opção:')

        #precisa arrumar os inputs para receber parametros
        match opcao:
            case '0':
                menu_aberto = False
            case '1':
                popula_banco()
            case '2':
                cria_admin()
            case '3':
                print('Insira abaixo a data inicial para pesquisar os vencedores:')
                dia = int(input('Digite o dia:'))
                mes = int(input('Digite o mes:'))
                ano = int(input('Digite o ano:'))

                consulta = Estatistica.objects.buscar_corredores_vencedores(date(ano,mes,dia))
                print(consulta)

            case '4':
                print('1 - Corrida\n'
                      '2 - Basquetebol\n'
                      '3 - Futebol')

                opcao = input('Escolha um esporte para pesquisar em eventos oficiais:')

                esporte = ''
                if opcao == 1:
                    esporte ='Running'
                if opcao == 2:
                    esporte ='Basketball'
                if opcao == 3:
                    esporte ='Football'

                consulta = Estatistica.objects.buscar_maiores_pontuadores_eventos_oficiais(esporte)
                print(consulta)
            case '5':
                eventos = Evento.objects.all()
                for i in range(eventos.__len__()):
                    print(f'ID:{eventos[i].pk} {eventos[i].nome}')

                id_evento = int(input('Digite o id do evento desejado:'))

                # Encontra o evento
                evento_encontrado = ''
                for i in range(eventos.__len__()):
                    if id_evento == eventos[i].pk:
                        evento_encontrado = eventos[i]

                if evento_encontrado == '':
                    print('Id inválido!')
                else:
                    consulta = (Estatistica.objects.buscar_participantes(evento_encontrado))
                    print(consulta)

            case '6':
                print('Insira abaixo a data para :')
                dia = int(input('Digite o dia:'))
                mes = int(input('Digite o mes:'))
                ano = int(input('Digite o ano:'))

                consulta = Estatistica.objects.buscar_evento_participantes_estrangeiros(date(ano, mes, dia))
                print(consulta)
"""


#if __name__ == '__main__':
    #create_basic_relacionamentos()
    #read_publications()
    #insert_revista()
    #find_revista()