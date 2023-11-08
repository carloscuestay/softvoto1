from dataclasses import field
from rest_framework import serializers
from  backend.models import Registro

class BackendSerializer(serializers.ModelSerializer):
    creado = serializers.ReadOnlyField()
    completado =serializers.ReadOnlyField()
    
    class Meta:
        model = Registro
        fields = ['id', 'titulo', 'descripcion', 'creado', 'completado']
        