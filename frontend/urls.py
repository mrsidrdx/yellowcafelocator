from . import views
from django.urls import path
from .views import LoginPage, HomePage

urlpatterns = [
    path('signin/', LoginPage.as_view(), name='login-page'),
    path('home/', HomePage.as_view(), name='home-page'),
]