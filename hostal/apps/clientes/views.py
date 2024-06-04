from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteCrearLista(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
"""GET: Lista todos los clientes POST: Crea un nuevo cliente"""

class ClienteDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
"""
    GET: Recupera un cliente específico
    PUT: Actualiza un cliente específico
    PATCH: Actualiza parcialmente un cliente específico
    DELETE: Elimina un cliente específico
    """