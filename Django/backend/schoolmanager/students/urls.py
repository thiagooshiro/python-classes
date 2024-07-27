from django.urls import path
from .views import StudentListView, StudentDetailView

# As rotas utilizam uma "view" como referência, a rota "/students" tem como referência a view "StudentDetailView", ou seja, quando uma requisição for feita para essa rota quem irá processar essa requisa será essa classe.

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]
