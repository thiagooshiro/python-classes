from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Students
import json

# Aqui estamos usando o decorator @csrf_exempt para que o Django não bloqueie as requisições que venham de origens não autenticadas.


#A classe StudentListView lida com dois tipos de requisição: "get" para obter a lista de todos os estudantes matriculados;

class StudentListView(View):
    def get(self, request):
        students = list(Students.objects.values())
        return JsonResponse(students, safe=False)
    
    
    @method_decorator(csrf_exempt, name="dispatch")
    def post(self, request):
        try:
            data = json.loads(request.body)
            student = Students.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                age=data['age'],
                registration=data['registration']
            )
            return JsonResponse({"id": student.id, "name": student.first_name, "message": "Student created successfully"})
        except(KeyError):
            return JsonResponse({ "error": "Requisição MAU FEITA!"}, status=400)
class StudentDetailView(View):
    def get(self, request, pk):
        try:
            student = Students.objects.get(pk=pk)
            return JsonResponse({
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "age": student.age,
                "registration": student.registration,
            })
        except Students.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)
    
    @csrf_exempt
    def put(self, request, pk):
        try:
            student = Students.objects.get(pk=pk)
            data = json.loads(request.body)
            student.first_name = data['first_name']
            student.last_name = data['last_name']
            student.email = data['email']
            student.age = data['age']
            student.registration = data['registration']
            student.save()
            return JsonResponse({"message": "Student updated successfully"})
        except Students.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

    @csrf_exempt
    def delete(self, request, pk):
        try:
            student = Students.objects.get(pk=pk)
            student.delete()
            return JsonResponse({"message": "Student deleted successfully"})
        except Students.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)
