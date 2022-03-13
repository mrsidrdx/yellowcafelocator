from . import views
from django.urls import path
from .views import LoginAPI, UserLocationsListAPI
from knox import views as knox_views

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='user-login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('user-locations/', UserLocationsListAPI.as_view(), name='user-locations'),
]