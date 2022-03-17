from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
 
class LoginPage(TemplateView):
    template_name = 'frontend/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home/')
        return super().get(request)

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/home.html'