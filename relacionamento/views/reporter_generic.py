from ..models.reporter import Reporter
from ..forms.reporter import ReporterForm
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
import random
import string
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ReporterListGeneric(ListView):
    model = Reporter
    template_name = 'reporter/list.html'
    context_object_name = 'lista' #nome da variavel utilizada no for do template
    queryset = Reporter.objects.all()#para fazer uma consulta especifica
    #queryset é um atributo de classe opcional, que sobreescreve a consulta padrão(que seria todos os objetos)
    #ordering = '-nome'

    def get_queryset(self):
        #ele tem o mesmo principio do queryset(se voce sobreescreve o metodo, não precisa da variavel)
        objetos = list(Reporter.objects.find_by_name('Lucas'))
        outros_objetos = list(Reporter.objects.find_by_name('Joao'))
        objetos.extend(outros_objetos)
        #objetos.sort(key=lambda reporter: reporter.nome, reverse=True)
        def key(reporter): return reporter.nome
        return objetos

class ReporterDetailGeneric(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'relacionamento.view_reporter'

    model = Reporter
    fields = '__all__'
    template_name = 'reporter/read.html'
    success_url = reverse_lazy('relacionamento:classe_reporter') #ação de sucesso no template

class ReporterDeleteGeneric(DeleteView):
    model = Reporter
    fields = '__all__'
    template_name = 'reporter/delete.html'
    success_url = reverse_lazy('relacionamento:classe_reporter')

class ReporterUpdateGeneric(UpdateView):
    model = Reporter
    template_name = 'reporter/update.html'
    form_class = ReporterForm
    success_url = reverse_lazy('relacionamento:classe_reporter')

class ReporterCreateGeneric(CreateView):
    model = Reporter
    template_name = 'reporter/create_simple.html'
    form_class = ReporterForm
    success_url = reverse_lazy('relacionamento:classe_reporter')