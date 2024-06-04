from django.test import TestCase
from .models import Cliente
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre='Juan',
            apellido='Pérez',
            direccion='Calle Falsa 123',
            telefono='123456789',
            correo_electronico='juan.perez@example.com'
        )

    def test_cliente_creacion(self):
        self.assertEqual(self.cliente.nombre, 'Juan')
        self.assertEqual(self.cliente.apellido, 'Pérez')
        self.assertEqual(self.cliente.direccion, 'Calle Falsa 123')
        self.assertEqual(self.cliente.telefono, '123456789')
        self.assertEqual(self.cliente.correo_electronico, 'juan.perez@example.com')

class ClienteAPITest(APITestCase):
    
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre='Juan',
            apellido='Pérez',
            direccion='Calle Falsa 123',
            telefono='123456789',
            correo_electronico='juan.perez@example.com'
        )
        self.list_url = reverse('listar_clientes')
        self.detail_url = reverse('detalle_cliente', kwargs={'pk': self.cliente.pk})

    def test_listar_clientes(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_detalle_cliente(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Juan')

    def test_crear_cliente(self):
        data = {
            'nombre': 'Ana',
            'apellido': 'Gómez',
            'direccion': 'Calle Verdadera 456',
            'telefono': '987654321',
            'correo_electronico': 'ana.gomez@example.com'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], 'Ana')

    def test_actualizar_cliente(self):
        data = {
            'nombre': 'Juanito',
            'apellido': 'Pérez',
            'direccion': 'Calle Falsa 123',
            'telefono': '123456789',
            'correo_electronico': 'juan.perez@example.com'
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Juanito')

    def test_parcial_actualizar_cliente(self):
        data = {'nombre': 'Juanito'}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Juanito')

    def test_eliminar_cliente(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Cliente.objects.filter(pk=self.cliente.pk).exists())
    
    def test_permisos_no_autorizados(self):
        # Crear un nuevo cliente sin autenticación debería fallar
        self.client.logout()
        data = {
            'nombre': 'Carlos',
            'apellido': 'López',
            'direccion': 'Calle Real 789',
            'telefono': '123456789',
            'correo_electronico': 'carlos.lopez@example.com'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Intentar eliminar un cliente sin autenticación debería fallar
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)