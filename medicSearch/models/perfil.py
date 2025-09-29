from medicSearch.models import *

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    papel = models.IntegerField(choices=ROLE_CHOICE, default=3, verbose_name='Papel')
    nascimento = models.DateField(default=None, null=True, verbose_name='Nascimento')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, blank=True)
    favoritos = models.ManyToManyField(User, related_name='favoritos', verbose_name='Favoritos')
    especialidade = models.ManyToManyField('Especialidade', related_name='Especialidade', verbose_name='Especialidade')
    endereco = models.ManyToManyField('Endereco', related_name='Endereço', verbose_name='Endereço')

    def __str__(self):
        return '{}'.format(self.usuario.username)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Perfil.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
    