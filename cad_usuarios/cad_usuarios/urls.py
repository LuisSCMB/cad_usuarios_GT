from app_cad_usuarios import views
from django.urls import path

urlpatterns = [
    #rota , view responsavel, nome de rederencia

    path('',views.home,name='home'),#String vazia é a home da pagina, 'Home' é o nome do arquivo no views do app .py
]
