from medicSearch.models import *

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, null=True, related_name='state', on_delete=models.SET_NULL, verbose_name='Estado')
    nome = models.CharField(null=False, max_length=20, verbose_name='Nome')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.estado.nome)