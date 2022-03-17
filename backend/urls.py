from . import views
from django.urls import path
from .views import LoginView, LogoutView, UserLocationsListAPI

urlpatterns = [
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    path('user-locations/', UserLocationsListAPI.as_view(), name='user-locations'),
]