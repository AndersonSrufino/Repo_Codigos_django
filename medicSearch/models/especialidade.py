from medicSearch.models import *

class Especialidade(models.Model):
    nome = models.CharField(null=False, max_length=100, verbose_name='Nome')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome)
    