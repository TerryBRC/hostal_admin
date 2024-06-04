from rest_framework import serializers 
from .models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    model = Factura
    fields = '__all__'

    fecha_emision = serializers.DateTimeField(format=f"%d-%m-%Y %H:%M:%S")