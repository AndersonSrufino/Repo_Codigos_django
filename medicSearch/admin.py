from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('usuario', 'papel', 'nascimento')
    list_filter = ('usuario__is_active',)
    #readonly_fields = ('usuario',)
    search_fields = ('usuario__username',)
    fieldsets = (
        ('Usuário',{
            'fields':('usuario','nascimento','image',)
        }),
        ('Função',{
            'fields':('papel',)
        }),
        ('Extras',{
            'fields':('especialidade','endereco',)
        }),
    )

admin.site.register(Perfil, ProfileAdmin)

admin.site.register(Endereco)
admin.site.register(Dia_da_semana)
admin.site.register(Avaliacao)
admin.site.register(Especialidade)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
