from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Usuario
from django.dispatch import receiver


@receiver(post_save, sender=User)
def CriaPerfil(sender, instance, created, **kwags):
    if created:
        Perfil.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def SalvaPerfil(sender, instance, **kwags):
    instance.usuario.save()
