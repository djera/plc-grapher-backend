from channels import Group
from packages.serializers import OutgoingPackageSerializer
import json, time
from packages.serializers import IncomingPackageSerializer
import uuid
from orders.serializers import OrderSerializer, LamellaSerializer

def order_to_produce(order):
    Group("control").send({
        'text': json.dumps({
            'type': "order-to-produce",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(OrderSerializer(order).data),
        })
    })


def order_to_remove_from_queue(order):
    Group("control").send({
        'text': json.dumps({
            'type': "order-to-remove-from-queue",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(OrderSerializer(order).data),
        })
    })

def scanner_status():
    Group("web").send({
        'text': json.dumps({
            'type': "scanner-status",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '',
        })
    })

def send_incoming_package_created(incomingPackage):
    print ("sending incoming package scanned to WS")
    Group("control").send({
        'text': json.dumps({
            'type': "package-scanned",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(IncomingPackageSerializer(
                incomingPackage).data),
        })
    })

def send_incoming_package_created_prodline(incomingPackage):
    print ("sending incoming package from prodline to WS")
    Group("control").send({
        'text': json.dumps({
            'type': "package-added",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(IncomingPackageSerializer(
                incomingPackage).data),
        })
    })

def send_incoming_package_unset_prodline(incomingPackage):
    print ("sending loaded incoming package unset from prodline to WS")
    Group("control").send({
        'text': json.dumps({
            'type': "package-unset",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(IncomingPackageSerializer(
                incomingPackage).data),
        })
    })

def send_scanned_package_unset_prodline(incomingPackage):
    print ("sending scanned incoming package unset from prodline to WS")
    Group("control").send({
        'text': json.dumps({
            'type': "scanned-package-unset",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(IncomingPackageSerializer(
                incomingPackage).data),
        })
    })

def ws_s1_delete_lamella(id):
    print ("deleting lamella in s1")
    Group("control").send({
        'text': json.dumps({
            'type': "s1-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s2_delete_lamella(id):
    print ("deleting lamella in s2")
    Group("control").send({
        'text': json.dumps({
            'type': "s2-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s3_delete_lamella(id):
    print ("deleting lamella in s3")
    Group("control").send({
        'text': json.dumps({
            'type': "s3-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s4_delete_lamella(id):
    print ("deleting lamella in s4")
    Group("control").send({
        'text': json.dumps({
            'type': "s4-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s5_delete_lamella(id):
    print ("deleting lamella in s5")
    Group("control").send({
        'text': json.dumps({
            'type': "s5-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s6_delete_lamella(id):
    print ("deleting lamella in s6")
    Group("control").send({
        'text': json.dumps({
            'type': "s6-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s7_delete_lamella(id):
    print ("deleting lamella in s7")
    Group("control").send({
        'text': json.dumps({
            'type': "s7-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s8_delete_lamella(id):
    print ("deleting lamella in s8")
    Group("control").send({
        'text': json.dumps({
            'type': "s8-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_etage_delete_lamella(id):
    print ("deleting lamella in etage")
    Group("control").send({
        'text': json.dumps({
            'type': "etage-delete-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_duplicate_etage_lamella(id):
    print ("duplicating lamella in etage")
    Group("control").send({
        'text': json.dumps({
            'type': "etage-duplicate-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_delete_zinc_lamella(id):
    print ("deleting zinc lamella")
    Group("control").send({
        'text': json.dumps({
            'type': "delete-zinc-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_toggle_exit_strategy():
    print ("toggling exit strategy")
    Group("control").send({
        'text': json.dumps({
            'type': "toggle-exit-strategy",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '',
        })
    })

def unload(id):
    print ("unloading package")
    Group("control").send({
        'text': json.dumps({
            'type': "unload-package",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_move_to_2nd_halfetage(id):
    print ("moving to 2nd halfetage")
    Group("control").send({
        'text': json.dumps({
            'type': "move-to-2nd-halfetage",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_move1_to_2nd_halfetage(id):
    print ("moving1 to 2nd halfetage")
    Group("control").send({
        'text': json.dumps({
            'type': "move1-to-2nd-halfetage",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s8_duplicate_lamella(id):
    print ("moving to 2nd halfetage")
    Group("control").send({
        'text': json.dumps({
            'type': "s8-duplicate-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_s4_duplicate_lamella(id):
    print ("s4 duplicate lamella")
    Group("control").send({
        'text': json.dumps({
            'type': "s4-duplicate-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_set_superplan_dimensions(dimensions):
    print ("setting superpan dimensions")
    Group("control").send({
        'text': json.dumps({
            'type': "set-superplan-dimensions",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(dimensions),
        })
    })

def ws_boardbeforeentrancepaternoster():
    print ("setting board before entrance paternoster")
    Group("control").send({
        'text': json.dumps({
            'type': "board-before-entrance-paternoster",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_deletelamellatoetage():
    print ("setting delete lamella to etage")
    Group("control").send({
        'text': json.dumps({
            'type': "delete-lamella-to-etage",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_boardwenttoetage1():
    print ("setting board went to etage 1")
    Group("control").send({
        'text': json.dumps({
            'type': "board-went-to-etage-1",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_boardwenttoetage2():
    print ("setting board went to etage 2")
    Group("control").send({
        'text': json.dumps({
            'type': "board-went-to-etage-2",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_boardwenttoetage3():
    print ("setting board went to etage 3")
    Group("control").send({
        'text': json.dumps({
            'type': "board-went-to-etage-3",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_forcefinishorder():
    print ("force finishing order")
    Group("control").send({
        'text': json.dumps({
            'type': "force-finish-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_makeoneadditionallamella():
    print ("make one additional lamella")
    Group("control").send({
        'text': json.dumps({
            'type': "make-one-additional-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_makeonelesslamella():
    print ("make one less lamella")
    Group("control").send({
        'text': json.dumps({
            'type': "make-one-less-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_enablehalter():
    print ("enable halter")
    Group("control").send({
        'text': json.dumps({
            'type': "enable-halter",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_bodenlagerdelete(id):
    print ("bodenlager delete")
    Group("control").send({
        'text': json.dumps({
            'type': "bodenlager-delete",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_bodenlagermove(id):
    print ("bodenlager move")
    Group("control").send({
        'text': json.dumps({
            'type': "bodenlager-move",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_bodenlagerduplicate(id):
    print ("bodenlager duplicate")
    Group("control").send({
        'text': json.dumps({
            'type': "bodenlager-duplicate",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_forcemoveto2ndkette():
    print ("bodenlager force move to 2nd kette")
    Group("control").send({
        'text': json.dumps({
            'type': "force-move-to-2nd-kette",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_stopclearingxcut():
    print ("stop clearing xcut")
    Group("control").send({
        'text': json.dumps({
            'type': "stop-clearing-xcut",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_stopwaitingforzincleer():
    print ("stop waiting for zinc leer")
    Group("control").send({
        'text': json.dumps({
            'type': "stop-waiting-for-zinc-leer",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_createlamellaonwalze():
    print ("create lamella on walze")
    Group("control").send({
        'text': json.dumps({
            'type': "create-lamella-on-walze",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_createlamellafromorder():
    print ("create lamella from order")
    Group("control").send({
        'text': json.dumps({
            'type': "create-lamella-from-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_setxcut2oversize(oversize):
    print ("setting xcut2 oversize")
    Group("control").send({
        'text': json.dumps({
            'type': "set-xcut2-oversize",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(oversize),
        })
    })

def ws_setdryingtime(oversize):
    print ("setting drying time")
    Group("control").send({
        'text': json.dumps({
            'type': "set-drying-time",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(oversize),
        })
    })

def ws_clearbodenlagerorder():
    print ("clearing bodenlager order")
    Group("control").send({
        'text': json.dumps({
            'type': "clear-bodenlager-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_physicallymoveto2nd(id):
    print ("clearing bodenlager order")
    Group("control").send({
        'text': json.dumps({
            'type': "physically-move-to-2nd",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })


def ws_resendlamellatoetage():
    print ("resendlamellatoetage")
    Group("control").send({
        'text': json.dumps({
            'type': "resend-lamella-to-etage",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_deletealls1():
    print ("ws_deletealls1")
    Group("control").send({
        'text': json.dumps({
            'type': "delete-all-s1",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_removeboardfromxcut2order():
    print ("ws_removeboardfromxcut2order")
    Group("control").send({
        'text': json.dumps({
            'type': "remove-board-from-xcut2-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_addboardtoxcut2order():
    print ("ws_addboardtoxcut2order")
    Group("control").send({
        'text': json.dumps({
            'type': "add-board-to-xcut2-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_deletestackerpackage(id):
    print ("ws_deletestackerpackage")
    Group("control").send({
        'text': json.dumps({
            'type': "delete-stacker-package",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_duplicatevorhoblerlamella(id):
    print ("ws_duplicatevorhoblerlamella")
    Group("control").send({
        'text': json.dumps({
            'type': "duplicate-vorhobler-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'id\' : ' + str(id) + '}',
        })
    })

def ws_setglueid(string):
    print ("ws_setglueid")
    Group("control").send({
        'text': json.dumps({
            'type': "set-glue-id",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{ \'glueId\' : \'' + str(string) + '\'}',
        })
    })

def ws_testlamellaneededtoggle():
    print ("ws_testlamellaneededtoggle")
    Group("control").send({
        'text': json.dumps({
            'type': "test-lamella-needed-toggle",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_addboardtobodenlagerorder():
    print ("ws_addboardtobodenlagerorder")
    Group("control").send({
        'text': json.dumps({
            'type': "add-board-to-bodenlager-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_removeboardfrombodenlagerorder():
    print ("ws_removeboardtobodenlagerorder")
    Group("control").send({
        'text': json.dumps({
            'type': "remove-board-from-bodenlager-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_stopbodenlagerpackages():
    print ("ws_stopbodenlagerpackages")
    Group("control").send({
        'text': json.dumps({
            'type': "stop-bodenlager-packages",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': '{}',
        })
    })

def ws_reprintsticker(p):
    print ("ws_reprintsticker")
    Group("control").send({
        'text': json.dumps({
            'type': "reprint-sticker",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(OutgoingPackageSerializer(p).data),
        })
    })

def ws_simulator(p):
    print ("ws_simulator")
    Group("control").send({
        'text': json.dumps({
            'type': "simulator-command",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps({'running': p}),
        })
    })

def ws_command(p):
    print ("ws_command - state checker, sending command %s" % p)
    Group("control").send({
        'text': json.dumps({
            'type': p,
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': None,
        })
    })

def send_remove_order_from_queue(order):
    print ("send_remove_order_from_queue %s" % order.id)
    Group("control").send({
        'text': json.dumps({
            'type': "remove-order-from-queue",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(OrderSerializer(order).data),
        })
    })

def send_repair_lamellas_to_order(lamellas, order):
    Group("control").send({
        'text': json.dumps({
            'type': "remove-lamella-from-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps({'order': OrderSerializer(order).data, 'lamellas': LamellaSerializer(lamellas, many=True).data}),
        })
    })

def send_repair_lamella_to_order(lamella, order):
    Group("control").send({
        'text': json.dumps({
            'type': "order-repair-for-lamella",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps({'order': OrderSerializer(order).data, 'lamella': LamellaSerializer(lamella).data}),
        })
    })

def restart_order(order):
    Group("control").send({
        'text': json.dumps({
            'type': "restart-order",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps(OrderSerializer(order).data),
        })
    })


def current_lamella_finished():
    Group("control").send({
        'text': json.dumps({
            'type': "lamella-cut",
            'timestamp': int(time.time()),
            'sent': True,
            'guid': str(uuid.uuid4()),
            'data': json.dumps({}),
        })
    })