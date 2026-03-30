from ..models.reporter import Reporter
from ..forms.reporter import ReporterForm
from django.shortcuts import render, get_object_or_404, redirect
import random
import string
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required

@require_http_methods(["GET"])
def reporter_list(request):
    reporters = Reporter.objects.all()
    contexto = {
        'lista': reporters
    }
    return  render(request, 'reporter/list.html', contexto)


@login_required
@permission_required('relacionamento.view_reporter', raise_exception=True)
@require_http_methods(["GET"])
def reporter_detail(request,pk):
    busca = Reporter.objects.get(id=pk)
    contexto = {
        'reporter': busca
    }
    return render(request, 'reporter/read.html', contexto)

@login_required
@permission_required('relacionamento.delete_reporter', raise_exception=True)
@require_http_methods(["GET", "POST"])
def reporter_delete(request,pk):
    busca = get_object_or_404(Reporter, id=pk)
    try:
        if request.method == 'POST':
            v_reporter_id = request.POST.get('reporter_id', None)
            if int(v_reporter_id) == pk:
                busca.delete()
                return redirect('relacionamento:reporter')
        else:
            contexto = {
                'reporter': busca
            }
            return render(request, 'reporter/delete.html', contexto)
    except Exception as e:
        contexto = {}
        print(e)
        return render(request, 'reporter/list.html', contexto)

@require_http_methods(["POST"])
def reporter_generate_name(request, pk):
    busca = get_object_or_404(Reporter, id=pk)
    try:
        letters = string.ascii_letters + string.digits
        busca.nome = ''.join(random.choice(letters) for i in range(10))
        busca.save()
        return redirect('relacionamento:reporter')
    except Exception as e:
        print(e)
        print(f'Erro ao gerar o nome da {busca.nome}')
        return redirect('relacionamento:reporter')

@login_required
@permission_required('relacionamento.add_reporter', raise_exception=True)
@require_http_methods(["GET", "POST"])
def reporter_create(request):
    if request.method == 'POST':
        '''quando o usuário preenche o formulário para ser salvo no sistema'''
        form = ReporterForm(request.POST)
        if form.is_valid():
            #isso chama as validações
            form.save()
            return  redirect('relacionamento:reporter')
    else:
        '''quando o usuário chega na página, mostrando u mformulário vazio'''
        form = ReporterForm()

    context = {'form': form}

    return render(request, 'reporter/create_simple.html', context)

@login_required
@permission_required('relacionamento.change_reporter', raise_exception=True)
@require_http_methods(["GET", "POST"])
def reporter_update(request, pk):
    busca = get_object_or_404(Reporter, pk=pk)
    if request.method == 'POST':
        '''quando o usuário altera o formulário para ser salvo no sistema'''
        form = ReporterForm(request.POST, instance=busca)
        if form.is_valid():
            #isso chama as validações
            form.save()
            return  redirect('relacionamento:reporter')
    else:
        '''quando o usuário chega na página, mostra o formulario com os dados do objeto'''
        form = ReporterForm(instance=busca)

    context = {'form': form,
               'objeto': busca}

    return render(request, 'reporter/update.html', context)
