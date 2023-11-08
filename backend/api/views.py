from django.shortcuts import render
from rest_framework import generics
from .serializers import BackendSerializer
from backend.models import Registro


class TodoListCreate(generics.ListCreateAPIView):
    
    def get_queryset(self):
        user = self.request.user
        return Registro.objects.filter(user=user).order_by('-creado')
    
    

