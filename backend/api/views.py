from rest_framework import generics, permissions
from .serializers import BackendSerializer, TodoToggleCompleteSerializer
from backend.models import Registro


class TodoList(generics.ListAPIView):
    serializer_class = BackendSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Registro.objects.filter(user=user).order_by('-creado')
    
class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = BackendSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Registro.objects.filter(user=user).order_by('-creado')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    
    
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BackendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Registro.objects.filter(user=user)
    
class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        return Registro.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()