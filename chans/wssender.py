from channels import Group
import json, time
import uuid
def test_ws():
    Group("web").send({
        'text': json.dumps({
            'type': "test_ws",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '',
        })
    })

def graph_update(data):
    Group("web").send({
        'text': json.dumps({
            'type': "graph_data",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': data,
        })
    })
