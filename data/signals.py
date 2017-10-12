from django.db.models.signals import post_save
from django.dispatch import receiver
from data.models import HexData
from data.models import DataModelConfig, VariableConfig
import binascii
from chans.wssender import graph_update

@receiver(post_save, sender=HexData)
def send_graph_data(sender, instance=None, created=False, **kwargs):
    if instance is not None:

        config = DataModelConfig.objects.filter(user=instance.user).first()
        variables = VariableConfig.objects.filter(config=config)

        data = {}
        s = binascii.unhexlify(instance.hex_data)
        b = [ord(x) for x in s]
        b_len = len(b)
        for v in variables:
            if v.type == VariableConfig.TYPES[0][0]:
                if v.startByte < b_len:
                    print(str(b[v.startByte]) + ' % '  + str(pow(2, v.startBit)))
                    value = b[v.startByte] & pow(2, v.startBit)
                    data[v.name] = value

        data["timestamp"] = instance.added_at
        graph_update(data)