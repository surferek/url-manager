import pytest
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
)

from .models import UrlBind


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_shorten_create(client):
    post_data = {
        "url": "https://github.com/ellisonleao/pyshorteners/"
    }
    request = client.post('/shorten/', post_data)

    shorten_obj = UrlBind.objects.get(short_url=request.data['short_url'])
    expected_response = {
        "short_url": shorten_obj.short_url
    }

    assert request.status_code, HTTP_201_CREATED
    assert request.data, expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_shorten_create_the_same_url_twice(client):
    post_data = {
        "url": "https://github.com/ellisonleao/pyshorteners/"
    }
    request = client.post('/shorten/', post_data)
    shorten_obj = UrlBind.objects.get(short_url=request.data['short_url'])

    expected_response = {
        "url": "https://github.com/ellisonleao/pyshorteners/",
        "short_url": shorten_obj.short_url
    }
    request = client.post('/shorten/', post_data)

    assert request.status_code, HTTP_409_CONFLICT
    assert request.data, expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_shorten_create_validation_error(client):
    post_data = {
        "url": "For sure not URL"
    }
    request = client.post('/shorten/', post_data)

    assert request.status_code, HTTP_400_BAD_REQUEST


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_shorten_list(client, ulr_binder):
    request = client.get('/shorten/')
    expected_response = [{
        'id': 1,
        'url': 'https://realpython.com/1',
        'short_url': 'http://localhost:8000/test_1'
    }, {
        'id': 2,
        'url': 'https://realpython.com/2',
        'short_url': 'http://localhost:8000/test_2'
    }]

    assert request.status_code, HTTP_200_OK
    assert request.data, expected_response


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_shorten_retrieve(client, ulr_binder):
    request = client.get('/shorten/1/')
    expected_response = {
        'id': 1,
        'url': 'https://realpython.com/1',
        'short_url': 'http://localhost:8000/test_1'
    }
    assert request.status_code, HTTP_200_OK
    assert request.data, expected_response
