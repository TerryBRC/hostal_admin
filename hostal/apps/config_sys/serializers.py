from rest_framework import serializers
from .models import SysConfig

class SysConfigSerializer(serializers.ModelSerializer):
    class  Meta:
        model = SysConfig
        fields = '__all__'