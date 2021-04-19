from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Usuario
from django.dispatch import receiver


@receiver(post_save, sender=User)
def CriaPerfil(sender, instance, created, **kwags):
    if created:
        Usuario.objects.create(perfil=instance)


@receiver(post_save, sender=User)
def SalvaPerfil(sender, instance, **kwags):
    instance.perfil.save()
