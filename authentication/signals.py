from django.dispatch import Signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

user_sign_in = Signal(providing_args=["user", "request"])
user_registered = Signal(providing_args=["user", "request"])
user_sign_out = Signal(providing_args=["user", "request"])

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
