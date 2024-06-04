from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre',null=False,blank=False)
    apellido = models.CharField(max_length=100,verbose_name='Apellido',null=False,blank=False)
    direccion = models.CharField(max_length=255,verbose_name='Dirección',null=False,blank=False)
    telefono = models.CharField(max_length=20,verbose_name='Teléfono',null=False,blank=False)
    correo_electronico = models.EmailField(unique=True,null=True,verbose_name='E-mail',blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Registro',null=True)
    
    class Meta:
        verbose_name_plural = 'Clientes'
        db_table= 'cliente'

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo_electronico}"