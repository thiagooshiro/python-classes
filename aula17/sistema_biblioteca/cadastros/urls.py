from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/criar/', views.criar_usuario, name='criar_usuario'),
    path('usuarios/atualizar/<int:id>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
]
