from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


class TestStatusView(TestCase):
    fixtures = ["status.json"]

    def setUp(self):
        self.client = APIClient()
        self.data = {"name": "Fazendo", "color_hex": "#00ff00"}
        self.user = User.objects.create(username="desafio", password="desafio")

    def test_create_status_without_login_return_401(self):
        response = self.client.post("/status/", data=self.data)
        self.assertEqual(response.status_code, 401)

    def test_create_status_logged_return_201(self):
        self.client.force_login(self.user)
        response = self.client.post("/status/", data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_get_list_of_status(self):
        self.client.force_login(self.user)
        response = self.client.get("/status/").json()
        self.assertIn("results", response)
        self.assertGreater(len(response["results"]), 0)

    def test_get_specific_status(self):
        self.client.force_login(self.user)
        response = self.client.get("/status/", data={"id": 1}).json()
        self.assertIn("results", response)
        self.assertGreater(len(response["results"]), 0)
