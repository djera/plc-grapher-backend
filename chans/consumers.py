from channels import Group
from rest_framework.authtoken.models import Token
import re, json
from eventlog.models import Event
from django.utils import timezone
from datetime import datetime
import pytz
import math

def channel_session_user_from_headers(func):
    """
    Decorator that automatically transfers the user from HTTP sessions to
    channel-based sessions, and returns the user as message.user as well.
    Useful for things that consume e.g. websocket.connect
    """

    def inner(message, *args, **kwargs):
        query_string = message['query_string']
        token = re.sub("token=", '', query_string)
        token_obj = Token.objects.filter(key=token).first()
        user = None
        if token_obj is not None:
            user = token_obj.user
        message.user = user
        return func(message, *args, **kwargs)
    return inner


# Connected to websocket.connect
# @channel_session_user_from_headers
# @channel_session
def ws_add(message):
    room = re.sub("/websocket/", '', message.content['path'])
    print("Room:" + room)
    # print(message.user)

    # if message.user is not None:
    # message.channel_session['room'] = room
    # message.channel_session['user'] = message.user.id

    # message.channel_session.save()
    message.reply_channel.send({"accept": True})
    Group(str(room)).add(message.reply_channel)

    # else:
    #    Group(str(room)).discard(message.reply_channel)


# Connected to websocket.receive
# @channel_session
def ws_message(message):
    #print(message)
    pass

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("control").discard(message.reply_channel)
    global send
    send = False
