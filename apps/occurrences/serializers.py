from rest_framework import serializers

from .models import Occurrence, Road, Status


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ["name", "color_hex"]


class RoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Road
        fields = ["name", "uf_code", "length"]


# add new code below
class OccurrenceSerizaliser(serializers.HyperlinkedModelSerializer):
    road_name = serializers.SerializerMethodField("get_road_name")
    status_name = serializers.SerializerMethodField("get_status_name")

    def get_road_name(self, occurrence):
        return occurrence.road.name

    def get_status_name(self, occurrence):
        return occurrence.status.name

    class Meta:
        model = Occurrence
        fields = [
            "description",
            "road",
            "road_name",
            "km",
            "status",
            "status_name",
            "created_at",
            "updated_at",
        ]
