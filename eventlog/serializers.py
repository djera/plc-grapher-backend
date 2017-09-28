from rest_framework import serializers
from .models import Event
from authentication.serializers import CustomUserSerializerEvent

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
