# models.py
from medicSearch.models import *


class Dia_da_semana(models.Model):
    #nome = models.CharField(null=False, max_length=20, verbose_name="Nome")
    data = models.DateField(default=None, null=True, verbose_name='Data')
    status = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    #retorna a data formatada
    def data_formatada(self):
        #verifica se a data esta vazia
        if self.data:
            return self.data.strftime('%A - %d/%m/%y').capitalize()
        #retorna uma strig vazia ou outra msg se a data for nula
        return "Data não localizada"
    

    def __str__(self):
        return self.data_formatada()
