from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Usuario
import json

# Listar usuários (GET)
def listar_usuarios(request):
    if request.method == 'GET':
        usuarios = list(Usuario.objects.values())
        return JsonResponse(usuarios, safe=False)
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

# Detalhar usuário (GET por ID)
def detalhar_usuario(request, id):
    if request.method != 'GET':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    usuario = Usuario.objects.filter(id=id).first()
    if not usuario:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)

    return JsonResponse({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email})

# Criar usuário (POST)
@csrf_exempt
def criar_usuario(request):
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    try:
        data = json.loads(request.body)
        nome = data.get('nome', '').strip()
        email = data.get('email', '').strip()

        if not nome:
            return JsonResponse({'erro': 'Nome não pode estar vazio'}, status=400)

        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'erro': 'Email inválido'}, status=400)

        usuario = Usuario.objects.create(nome=nome, email=email)
        return JsonResponse({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'erro': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=400)

# Atualizar usuário (PUT)
@csrf_exempt
def atualizar_usuario(request, id):
    if request.method != 'PUT':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    usuario = Usuario.objects.filter(id=id).first()
    if not usuario:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)

    try:
        data = json.loads(request.body)
        nome = data.get('nome')
        email = data.get('email')

        if nome is not None:
            nome = nome.strip()
            if not nome:
                return JsonResponse({'erro': 'Nome não pode estar vazio'}, status=400)
            usuario.nome = nome

        if email is not None:
            email = email.strip()
            try:
                validate_email(email)
                usuario.email = email
            except ValidationError:
                return JsonResponse({'erro': 'Email inválido'}, status=400)

        usuario.save()
        return JsonResponse({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email})

    except json.JSONDecodeError:
        return JsonResponse({'erro': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'erro': str(e)}, status=400)

# Deletar usuário (DELETE)
@csrf_exempt
def deletar_usuario(request, id):
    if request.method != 'DELETE':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    usuario = Usuario.objects.filter(id=id).first()
    if not usuario:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)

    usuario.delete()
    return JsonResponse({'mensagem': 'Usuário deletado com sucesso'})
