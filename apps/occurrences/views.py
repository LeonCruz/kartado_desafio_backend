from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

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
    serializer_class = OccurrenceSerizaliser
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        road = self.request.query_params.get("road", None)
        status = self.request.query_params.get("status", None)

        if road is not None and status is not None:
            return Occurrence.objects.filter(road__name=road, status__name=status)
        elif road is not None:
            return Occurrence.objects.filter(road__name=road)
        elif status is not None:
            return Occurrence.objects.filter(status__name=status)
        else:
            return Occurrence.objects.all().order_by("created_at")
