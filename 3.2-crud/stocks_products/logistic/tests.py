from unittest import TestCase

from rest_framework.test import APIClient


class TestView(TestCase):
    def test_response(self):
        url = '/api/v1/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
