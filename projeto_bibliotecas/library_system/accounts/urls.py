from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:id>/', views.detalhar_usuario, name='detalhar_usuario'),
    path('usuarios/criar/', views.criar_usuario, name='criar_usuario'),
    path('usuarios/<int:id>/atualizar/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/<int:id>/deletar/', views.deletar_usuario, name='deletar_usuario'),
]
