import pytest

class TestSDK:
    def test_get_number(self, client):
        assert client.get_number(10) == 10
