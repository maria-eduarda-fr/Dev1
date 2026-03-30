from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class ProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        context = {
            'usuario': request.user,
        }
        return render(request, 'accounts/profile.html', context)