import token
from rest_framework import generics, permissions


from .serializers import BackendSerializer, TodoToggleCompleteSerializer
from backend.models import Registro
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
        
        
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error':'username taken. choose another username'},
            status=400)
    
    
    
    
    
    
    
    
    