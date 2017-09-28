from channels import Group
import time
from django.core.management.base import BaseCommand
import os
import re
from django.db.models import Q
from eventlog.models import Event
from orders.models import Order, Lamella
from orders.serializers import OrderSerializer
from chans.wssender import ws_simulator
from django.utils import timezone

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--running', type=str2bool, nargs='?',
                            const=True, default='True',
                            help="Timbertec import host down or not.")

    def handle(self, *args, **options):
        if 'running' in options:

            query= Q(type='import_host_down')|Q(type='import_host_up')
            last = Event.objects.filter(query).last()
            if options['running']:
                if last is None or last.type == 'import_host_down':
                    Event.objects.create(type='import_host_up')
            else:
                if last is None or last.type == 'import_host_up':
                    Event.objects.create(type='import_host_down')

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')