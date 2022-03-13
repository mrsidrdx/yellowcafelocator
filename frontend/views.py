from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
 
class LoginPage(TemplateView):
    template_name = 'frontend/login.html'

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/home.html'