from __future__ import unicode_literals

from django.db import models
from authentication.models import CustomUser

class HexData(models.Model):
    user = models.ForeignKey(CustomUser, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    hex_data = models.CharField(max_length=255)