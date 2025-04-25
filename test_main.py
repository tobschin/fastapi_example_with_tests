from http import HTTPStatus
from http.client import HTTPResponse
from unittest import TestCase

from starlette.testclient import TestClient
from main import app

class TestApi(TestCase):
    def test_root(self):
        with TestClient(app=app) as client:
            response = client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_read_items(self):
        with TestClient(app) as client:
            response = client.post('/', json={'val1': 'value1', 'val2': ['value2', 'value3']})

            self.assertEqual(HTTPStatus.OK, response.status_code)
            self.assertEqual({'val1': 'VALUE1', 'val2': ['VALUE2', 'VALUE3']}, response.json())

