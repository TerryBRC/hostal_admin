from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import TipoHabitacion
from .serializers import TipoHabitacionSerializer

class TipoHabitacionListarCrear(generics.ListCreateAPIView):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class TipoHabitacionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]