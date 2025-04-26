from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json

# Listar usuários (GET)
def listar_usuarios(request):
    usuarios = list(Usuario.objects.values())
    return JsonResponse(usuarios, safe=False)

# Criar usuário (POST)
@csrf_exempt
def criar_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = Usuario.objects.create(
                nome=data['nome'],
                email=data['email']
            )
            return JsonResponse({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email}, status=201)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

# Atualizar usuário (PUT)
@csrf_exempt
def atualizar_usuario(request, id):
    usuario = Usuario.objects.filter(id=id).first()
    if not usuario:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)
    
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            usuario.nome = data.get('nome', usuario.nome)
            usuario.email = data.get('email', usuario.email)
            usuario.save()
            return JsonResponse({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email})
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

# Deletar usuário (DELETE)
@csrf_exempt
def deletar_usuario(request, id):
    usuario = Usuario.objects.filter(id=id).first()
    if not usuario:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)
    
    if request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'mensagem': 'Usuário deletado com sucesso'})
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)
