from apps.occurrences.models import Occurrence, Road, Status
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class TestOccurrenceView(TestCase):
    fixtures = ["occurrences.json", "road.json", "status.json"]

    def setUp(self):
        self.client = APIClient()

        data_road = {"name": "BR-316", "uf_code": "15", "length": 300.0}
        road = Road.objects.create(**data_road)

        data_status = {"name": "Fazendo", "color_hex": "#00ff00"}
        status = Status.objects.create(**data_status)

        self.user = User.objects.create(username="desafio", password="desafio")

        self.data_occurrences = {
            "description": "Quiquia modi etincidunt modi.",
            "road": reverse("road-detail", args=[road.id]),
            "km": 70,
            "status": reverse("status-detail", args=[status.id]),
        }

    def test_create_occurrence_without_login_return_401(self):
        response = self.client.post("/occurrences/", data=self.data_occurrences)
        self.assertEqual(response.status_code, 401)

    def test_create_occurrence_logged_return_201(self):
        self.client.force_login(self.user)

        response = self.client.post("/occurrences/", data=self.data_occurrences)
        self.assertEqual(response.status_code, 201)

    def test_get_list_of_occurrences(self):
        self.client.force_login(self.user)

        response = self.client.get("/occurrences/").json()
        self.assertIn("results", response)
        self.assertGreater(len(response["results"]), 0)

    def test_get_specific_occurrence(self):
        self.client.force_login(self.user)

        response = self.client.get("/occurrences/", data={"id": 1}).json()
        self.assertIn("results", response)
        self.assertGreater(len(response["results"]), 0)

    def test_occurrence_has_fields_road_name_and_status_name(self):
        self.client.force_login(self.user)

        response = self.client.get("/occurrences/1/")
        self.assertContains(response, "road_name")
        self.assertContains(response, "status_name")
