from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

admin.site.register(ProfileAdmin)

admin.site.register(Perfil)    
admin.site.register(Endereco)
admin.site.register(Dia_da_semana)
admin.site.register(Avaliacao)
admin.site.register(Especialidade)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
