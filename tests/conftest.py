import pytest
from freezegun import freeze_time

from asynckraken.types import ApiConfig


@pytest.fixture
def mock_time():
    return freeze_time("2017-07-23 12:00:01")


@pytest.fixture
def key():
    return 'o1NXRpj0vA4RFbglrh7N9Mgwkar'\
           'ycfTDMY4yG32zu7nk4ZhtIJ4VpLoF'


@pytest.fixture
def secret():
    return 'VTKsodUqRc+T2Fe2hjqLr9rValrgkJ8'\
           '+jFXwm3wPk70IkKSG7XRXwySqYQSPuP7'\
           '/mNVyfgzYP7Ex9ObwVj6PYw=='


@pytest.fixture
def api_uri():
    return 'https://api.kraken.com'


@pytest.fixture
def api_version():
    return '0'


@pytest.fixture
def api_config(key, secret, api_uri, api_version):
    return ApiConfig(key, secret, api_uri, api_version)


@pytest.fixture
def corrupted_api_config(api_uri, api_version):
    return ApiConfig('wrong', 'wrong', api_uri, api_version)
