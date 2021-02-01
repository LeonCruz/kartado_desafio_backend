from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


class TestRoadView(TestCase):
    fixtures = ["road.json"]

    def setUp(self):
        self.client = APIClient()
        self.data = {"name": "BR-316", "uf_code": "15", "length": 300.0}
        self.user = User.objects.create(username="desafio", password="desafio")

    def test_create_road_without_login_return_401(self):
        response = self.client.post("/roads/", data=self.data)
        self.assertEqual(response.status_code, 401)

    def test_create_road_logged_return_201(self):
        self.client.force_login(self.user)
        response = self.client.post("/roads/", data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_get_list_of_roads(self):
        self.client.force_login(self.user)

        response = self.client.get("/roads/").json()
        self.assertIn("results", response)
        self.assertGreater(len(response["results"]), 0)

    def test_get_specific_road(self):
        self.client.force_login(self.user)

        response = self.client.get("/roads/", data={"id": 1}).json()
        self.assertIn("results", response)
        self.assertGreater(len(response["results"]), 0)
