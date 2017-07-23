from typing import NamedTuple


class ApiMethod:
    private = 'post'
    public = 'get'


class ApiConfig(NamedTuple):
    key: str
    secret: str
    uri: str
    version: str
