import pytest
import aiohttp

from asynckraken.client import Client


class TestClient:

    @pytest.fixture
    def client(self, key, secret, api_uri):
        return Client(key, secret, api_uri)

    def test_initialize(self, client, key, secret, api_uri):
        assert client.api.key == key
        assert client.api.secret == secret
        assert client.api.uri == api_uri
        assert client.timeout
        assert 'asynckraken' in client.headers['User-Agent']
        assert isinstance(client.session, aiohttp.ClientSession)

    def test_initialize_with_session(self, key, secret):
        session = aiohttp.ClientSession()
        client = Client(key, secret, session=session)
        assert client.session == session
