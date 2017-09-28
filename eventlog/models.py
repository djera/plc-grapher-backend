from __future__ import unicode_literals

from django.db import models
from authentication.models import CustomUser

class Event(models.Model):
    TYPES = (


    )

    type = models.CharField(max_length=50, choices=TYPES)
    user = models.ForeignKey(CustomUser, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
