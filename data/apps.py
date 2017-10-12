from __future__ import unicode_literals

from django.apps import AppConfig

class DataConfig(AppConfig):
    name = 'data'

    def ready(self):
        from data.signals import *