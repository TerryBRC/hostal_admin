from django.db import models

class SysConfig(models.Model):
    clave = models.CharField(max_length=50, unique=True,verbose_name='Clave',null=False,blank=False)
    valor = models.CharField(max_length=255,verbose_name='Valor',null=False,blank=False)

    class Meta:
        verbose_name_plural = 'Configuraciones'
        db_table = 'sysconfig'

    def __str__(self):
        return self.clave + ' / ' + self.valor