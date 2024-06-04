from rest_framework import serializers
from .models import TipoHabitacion

class TipoHabitacionSerializer(serializers.ModelSerializer):
    model = TipoHabitacion
    fields = '__all__'
    