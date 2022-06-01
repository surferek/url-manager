from django.test import TestCase
from rest_framework.test import APIClient


class ManageUrlTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_shorten_url(self):
        self.client = APIClient()
        post_data = {
            "url": "https://github.com/ellisonleao/pyshorteners/"
        }
        request = self.client.post('/url/shorten/', post_data)
        expected_response = {
            "short_url": "https://tinyurl.com/pglfnnj"
        }
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data, expected_response)

    def test_expand_url(self):
        self.client = APIClient()
        post_data = {
            "url": "https://tinyurl.com/pglfnnj"
        }
        request = self.client.post('/url/expand/', post_data)
        expected_response = {
            "long_url": "https://github.com/ellisonleao/pyshorteners/"
        }
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.data, expected_response)

    def test_shorten_url_validation_error(self):
        self.client = APIClient()
        post_data = {
            "url": "For sure not URL"
        }
        request = self.client.post('/url/shorten/', post_data)

        self.assertEqual(request.status_code, 400)

    def test_expand_url_validation_error(self):
        self.client = APIClient()
        post_data = {
            "url": "For sure not URL"
        }
        request = self.client.post('/url/expand/', post_data)

        self.assertEqual(request.status_code, 400)
