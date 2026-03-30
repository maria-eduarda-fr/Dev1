from ..forms.contact_form import ContactForm
from django.views import View
from django.shortcuts import render

class ContactView(View):
    @staticmethod
    def get(request):
        forms = ContactForm()
        context = {
            'form': forms,
            'url_form': 'class_contact'
        }
        return render(request, 'contact/page_contact.html', context)

    @staticmethod
    def post(request):
        forms = ContactForm(request.POST)
        if forms.is_valid():
            subject = forms.cleaned_data.get(
                'subject')  # validação - garantir que o usuario não inseriu dados não permitidos
            message = forms.cleaned_data.get('message')
            sender = forms.cleaned_data.get('sender')
            cc_myself = forms.cleaned_data.get('cc_myself')
            recipients = ['2024010427@aluno.restinga.ifrs.edu.br']  # receber os dados
            if cc_myself:
                recipients.append(sender)  # para enviar para o escritor tmb
            # TODO configurar o settings.py com os credenciais para envio do email
            # send_mail(subject, message, sender, recipients)        #chamada para o envio do email

            context = {
                'recipients': recipients,
                'form': forms
            }
            return render(request, 'contact/thanks.html', context)
        context = {'form': forms,
                   'url_form': 'contato'
                   # faz referencia ao name usado na url em especifico(para ter template reutilizaveis)
                   }
        return render(request, 'contact/page_contact.html', context)