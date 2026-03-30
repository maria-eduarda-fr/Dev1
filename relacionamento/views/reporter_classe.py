from ..models.reporter import Reporter
from ..forms.reporter import ReporterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import random
import string
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

class ReporterListView(View):
    @staticmethod
    def get(request):
        reporters = Reporter.objects.all()
        contexto = {
            'lista': reporters
        }
        return render(request, 'reporter/list.html', contexto)


class ReporterDetailView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'relacionamento.view_reporter'

    @staticmethod
    def get(request, pk):
        busca = Reporter.objects.get(id=pk)
        contexto = {
            'reporter': busca
        }
        return render(request, 'reporter/read.html', contexto)


class ReporterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'relacionamento.delete_reporter'
    @staticmethod
    def get(request, pk):
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

class ReporterCreateView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'relacionamento.add_reporter'

    @staticmethod
    def get(request):
        '''quando o usuário chega na página, mostrando u mformulário vazio'''
        form = ReporterForm()
        context = {'form': form}
        return render(request, 'reporter/create_simple.html', context)

    @staticmethod
    def post(request):
        '''quando o usuário preenche o formulário para ser salvo no sistema'''
        form = ReporterForm(request.POST)
        if form.is_valid():
            # isso chama as validações
            form.save()
            return redirect('relacionamento:reporter')

        context = {'form': form}

        return render(request, 'reporter/create_simple.html', context)


class ReporterGenerateNameView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'relacionamento.generate_name_reporter'

    @staticmethod
    def get(request, pk):
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

class ReporterUpdateView(View):
    @staticmethod
    def get(request,pk):
        busca = get_object_or_404(Reporter, pk=pk)
        '''quando o usuário chega na página, mostra o formulario com os dados do objeto'''
        form = ReporterForm(instance=busca)
        context = {'form': form,
                   'objeto': busca}
        return render(request, 'reporter/update.html', context)

    @staticmethod
    def post(request, pk):
        busca = get_object_or_404(Reporter, pk=pk)
        '''quando o usuário altera o formulário para ser salvo no sistema'''
        form = ReporterForm(request.POST, instance=busca)
        if form.is_valid():
            # isso chama as validações
            form.save()
            return redirect('relacionamento:reporter')
        context = {'form': form,
                   'objeto': busca}
        return render(request, 'reporter/update.html', context)