from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import (
    Participant
)
from .serializers import (
    ParticipantCreateSerializer,
    ParticipantRUDSerializer
)


class ParticipantsListCreate(ListCreateAPIView):
    """
    This API returns the list of participants when GET request is made, and creates
    a participant when a post request is made
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantCreateSerializer


class ParticipantRUD(RetrieveUpdateDestroyAPIView):
    """
    This API takes 'reference_number' as argument and retrieves, updates or delete
    the associated participant according to the request sent to it
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantRUDSerializer
