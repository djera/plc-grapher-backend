from rest_framework import serializers
from .models import HexData
from authentication.serializers import CustomUserSerializerEvent

class HexDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = HexData
        fields = ('hex_data',)
