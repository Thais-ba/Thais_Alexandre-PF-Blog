from django.urls import path
from . import views  # <--- ESSA LINHA RESOLVE O ERRO

app_name = 'messenger'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviar/', views.enviar_mensagem, name='enviar_mensagem'),
]