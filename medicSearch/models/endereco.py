from medicSearch.models import *

class Endereco(models.Model):
    bairro = models.ForeignKey(Bairro, null=True, related_name='Bairro', on_delete=models.SET_NULL)
    nome = models.CharField(null=False, max_length=20)
    endereco = models.CharField(null=False, max_length=255, verbose_name='Endereço')
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9 , decimal_places=7)
    horario_de_abertura = models.TimeField(verbose_name='Horário de abertura')
    horario_de_fechamento = models.TimeField(verbose_name='Horário de fechamento')
    dia_da_semana = models.ManyToManyField(Dia_da_semana, related_name='Dia_da_Semana')
    Telefone = models.CharField(null=True, max_length=10)
    whatsapp = models.CharField(null=True, max_length=11)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome)
