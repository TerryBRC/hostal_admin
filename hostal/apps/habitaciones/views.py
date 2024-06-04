from  rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from .models import Habitacion
from .serializers import HabitacionSerializer
from rest_framework import generics

class HabitacionListarHabitacion(generics.ListCreateAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]


class HabitacionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]