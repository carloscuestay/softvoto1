from django.shortcuts import render
from rest_framework import generics
from .serializers import BackendSerializer
from backend.models import Registro
from rest_framework.permissions import IsAuthenticated

class TodoList(generics.ListAPIView):
    serializer_class = BackendSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Registro.objects.filter(user=user).order_by('-creado')
    
class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = BackendSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Registro.objects.filter(user=user).order_by('-creado')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    
    

