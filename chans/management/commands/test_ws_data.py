from channels import Group
import time
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 0
        while True:
            print ("Sending test data")
            print(Group("control"))
            print(Group("control").channel_layer)
            Group("control").send({
                "text": "Test message" + str(i)
            })
            i = i + 1

            # Add a test channel to a test group
            t = ".."
            Group("control").add(t)
            # Send to the group
            Group("control").send({"value": 42})
            # Verify the message got into the destination channel
            # result = self.get_next_message("testchannel", require=True)
            # self.assertEqual(result['value'], 42)

            time.sleep(1)
