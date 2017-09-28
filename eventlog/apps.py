from __future__ import unicode_literals

from django.apps import AppConfig


class EventlogConfig(AppConfig):
    name = 'eventlog'

    def ready(self):
        from eventlog.receiver import *