from medicSearch.models import *

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, related_name='Avaliou', on_delete=models.CASCADE, verbose_name='Usuário')
    avaliacao_de_usuario = models.ForeignKey(User, related_name='Avaliado', on_delete=models.CASCADE, verbose_name='Avaliação do Usuário')
    value = models.DecimalField(max_digits=5, decimal_places=2)
    opnioes = models.TextField(null=True, verbose_name='Opniões')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return 'Avaliador: {} | Avaliado: {}'.format(self.usuario.first_name, self.avaliacao_de_usuario)