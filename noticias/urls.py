from . import views
from django.urls import path

urlpatterns = [
    # Exemplo de rota
    path('', views.home, name='home'),
]