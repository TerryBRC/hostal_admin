from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
"""     fecha_registro = serializers.DateTimeField(format=f"%d-%m-%Y %H:%M:%S") """