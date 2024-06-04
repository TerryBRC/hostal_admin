from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import generics
from .models import SysConfig
from .serializers import SysConfigSerializer

class SysConfigCrearLista(generics.ListCreateAPIView):
    queryset = SysConfig.objects.all()
    serializer_class = SysConfigSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class SysConfigDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysConfig.objects.all()
    serializer_class = SysConfigSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]