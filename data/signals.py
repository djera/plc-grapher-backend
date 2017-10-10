from django.dispatch import Signal
from django.db.models.signals import pre_save
from django.dispatch import receiver
from data.models import HexData
from django.conf import settings


@receiver(pre_save, sender=HexData)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        instance.user = self
