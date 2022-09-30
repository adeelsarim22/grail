from rest_framework import serializers
from .models import Participant


class ParticipantCreateSerializer(serializers.ModelSerializer):
    """
    This serializer is used for listing and creating participants
    """
    class Meta:
        model = Participant
        fields = "__all__"


class ParticipantRUDSerializer(serializers.ModelSerializer):
    """
    This is the serializer which is used for retrieve, put, patch, delete requests
    """
    class Meta:
        model = Participant
        exclude = ['reference_number']
