import pytest
from model_bakery import baker, seq
from rest_framework.test import APIClient


@pytest.fixture(name='client')
def fixture_client() -> APIClient:
    client = APIClient()
    return client


@pytest.fixture(name='ulr_binder')
def fixture_ulr_binder():
    baker.make(
        "manage_url.UrlBind",
        url=seq("https://realpython.com/"),
        short_url=seq("http://localhost:8000/test_"),
        _quantity=2
    )
