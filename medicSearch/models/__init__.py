from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = [
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
]

from .perfil import Perfil
from .dia_da_semana import Dia_da_semana
from .estado import Estado
from .cidade import Cidade
from .bairro import Bairro
from .endereco import Endereco
from .especialidade import Especialidade
from .avaliacao import Avaliacao