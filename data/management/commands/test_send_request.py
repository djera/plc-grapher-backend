from channels import Group
import time
from django.core.management.base import BaseCommand
import requests
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):

        if (hasattr(settings,'GRAPHER_URL') and hasattr(settings, 'GRAPHER_TOKEN')):
            post_data = {'hex_data': '012ABCDEF'}

            url = settings.GRAPHER_URL + '/api/v1/datalog/data/'
            headers = { 'Authorization': 'Token ' + settings.GRAPHER_TOKEN}
            print('post_data', post_data)
            print('url', url)
            print('headers', headers)
            response = requests.post(url, data=post_data, headers=headers)
            print(response.content)
        else:
            print('WARNING, NO GRAPHER URL OR TOKEN IN SETTINGS')