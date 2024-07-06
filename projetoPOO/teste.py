# books/views.py

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Book
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all().values()
        return JsonResponse(list(books), safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        book = Book.objects.create(**data)
        return JsonResponse({"id": book.id, "title": book.title, "author": book.author, "year": book.year}, status=201)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponseNotFound()
    
    if request.method == "GET":
        return JsonResponse({"id": book.id, "title": book.title, "author": book.author, "year": book.year})
    elif request.method == "PUT":
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(book, key, value)
        book.save()
        return JsonResponse({"id": book.id, "title": book.title, "author": book.author, "year": book.year})
    elif request.method == "DELETE":
        book.delete()
        return JsonResponse({}, status=204)
