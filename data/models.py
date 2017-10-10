from __future__ import unicode_literals

from django.db import models
from authentication.models import CustomUser
import binascii

class HexData(models.Model):
    user = models.ForeignKey(CustomUser, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    hex_data = models.CharField(max_length=255)


class DataModelConfig(models.Model):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(CustomUser)

    def __str__(self):
        return self.name

class VariableConfig(models.Model):
    TYPES = (
        ('bool', 'Boolean'),
        ('integer', 'Int'),
        ('double', 'DInt'),
        ('byte', 'Byte')
    )

    config = models.ForeignKey(DataModelConfig)
    type = models.CharField(max_length=50, choices=TYPES)
    name = models.CharField(max_length=50)
    startByte = models.IntegerField(default=0)
    startBit = models.IntegerField(default=0)
    endByte = models.IntegerField(default=-1)
    endBit = models.IntegerField(default=-1)