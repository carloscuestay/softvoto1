from django.shortcuts import render
from rest_framework import generics
from .serializers import BackendSerializer
from backend.models import Registro


class TodoList(generics.ListAPIView):
    serializer_class = BackendSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Registro.objects.filter(user=user).order_by('-creado')
    
class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = BackendSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Registro.objects.filter(user=user).order_by('-creado')
    
    

