from rest_framework import serializers
from .models import TipoHabitacion

class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'
    