import pytest
import binascii

from asynckraken.auth import KrakenHMAC


class TestKrakenHMAC:

    @pytest.fixture
    def params(self):
        return {
            'key': 'value',
            'foo': 'bar'
        }

    @pytest.fixture
    def urlpath(self):
        return 'path'

    @pytest.fixture
    def expected_nonce(self):
        return 1500811201000

    @pytest.fixture
    def expected_signature(self):
        return '5/8DC23Ml1dYYcvy3E59ZGUonYTPxk8LgX9YJjszm0Xn42'\
               'H6WVr0vXsvWhmRUA2M4VoqQfUb/Z3KEqMejO3Q/Q=='

    @pytest.fixture
    def expected_headers(self, expected_signature, api_config):
        return {
            'API-Key': api_config.key,
            'API-Sign': expected_signature,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    @pytest.fixture
    def kraken_hmac(self, params, urlpath, api_config, mock_time):
        with mock_time:
            return KrakenHMAC(params, urlpath, api_config)

    def test_initialize(self, kraken_hmac, params, urlpath, api_config):
        assert kraken_hmac.params == params
        assert kraken_hmac.urlpath == urlpath
        assert kraken_hmac.api_config == api_config
        assert kraken_hmac.nonce
        assert kraken_hmac.signature

    def test_nonce(self, kraken_hmac, expected_nonce):
        assert kraken_hmac.nonce == expected_nonce

    def test_headers(self, kraken_hmac, expected_headers):
        assert kraken_hmac.headers == expected_headers

    def test_wrong_key_or_secret(self, params, urlpath, corrupted_api_config):
        with pytest.raises(binascii.Error):
            KrakenHMAC(params, urlpath, corrupted_api_config)

    @pytest.mark.parametrize(
        "params,urlpath,expected_signature", [
            (
                {},
                'path',
                'WabfjWecs7QETUkvFa3/k4EJ+MEnojVtB6Oyf50Vwf+'
                'hu9cx0jK7FTLXkbWfIwpu9W1iCZsWe5gRRWCBHFETOg=='
            ),
            (
                {'key': 'value'},
                'path',
                'lwd/kFPqM9OF4U/NE6fQ7cOJPegQS1LvbGS6J7LViuiU'
                '2pdK3UdWgMV9CTMe3NApJcDk/MfB/Lv60YWzzjx2lg=='
            ),
            (
                {'key': 'value', 'foo': 'bar'},
                'path',
                '5/8DC23Ml1dYYcvy3E59ZGUonYTPxk8LgX9YJjszm0Xn'
                '42H6WVr0vXsvWhmRUA2M4VoqQfUb/Z3KEqMejO3Q/Q=='
            ),
            (
                {'key': 'value'},
                'another/path/to_resouce',
                'ZxzN4L0rcAPrk2lS/faIgwCm3lx990VC1VXBBQ6CQxk1'
                'KP5ZAezkXQfryTrwM2nk0icmSCpvl+ila6cj3sgghw=='
            )
        ]
    )
    def test_signature(
        self, params, urlpath, expected_signature, mock_time, api_config
    ):
        with mock_time:
            auth = KrakenHMAC(params, urlpath, api_config)
        assert auth.signature == expected_signature
