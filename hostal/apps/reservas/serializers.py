from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    model = Reserva
    fields = '__all__'
    fecha_entrada = serializers.DateTimeField(format=f"%d-%m-%Y %H:%M:%S")
    fecha_salida = serializers.DateTimeField(format=f"%d-%m-%Y %H:%M:%S")
    fecha_creacion = serializers.DateTimeField(format=f"%d-%m-%Y %H:%M:%S")
    fecha_modificacion = serializers.DateTimeField(format=f"%d-%m-%Y %H:%M:%S")