from rest_framework import serializers 
from .models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    fecha_emision = serializers.DateTimeField(format=f"%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Factura
        fields = '__all__'
