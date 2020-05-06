import pytest
from sdk.client import Client


@pytest.fixture
def client() -> Client:
    client = Client()

    yield client
