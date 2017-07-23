class TestApiConfig:

    def test_initialize(self, api_config, key, secret, api_uri, api_version):
        assert api_config.key == key
        assert api_config.secret == secret
        assert api_config.uri == api_uri
        assert api_config.version == api_version
