from medicSearch.models import *

class Bairro(models.Model):
    cidade = models.ForeignKey(Cidade, null=True, related_name='Cidade', on_delete=models.SET_NULL, verbose_name='Cidade')
    nome = models.CharField(null=False, max_length=20, verbose_name='Nome')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.cidade.nome)