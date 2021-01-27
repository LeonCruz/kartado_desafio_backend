from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Occurrence, Road, Status
from .serializers import OccurrenceSerizaliser, RoadSerializer, StatusSerializer


class RoadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roads to be viewed or edited.
    """

    queryset = Road.objects.all().order_by("name")
    serializer_class = RoadSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows status to be viewed or edited.
    """

    queryset = Status.objects.all().order_by("name")
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]


# add new code below
class OccurrenceView(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerizaliser
    permission_classes = [permissions.IsAuthenticated]
