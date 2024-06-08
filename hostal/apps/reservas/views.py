from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from .serializers import ReservaSerializer
from .models import Reserva



class ReservaListarCrear(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class ReservaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]