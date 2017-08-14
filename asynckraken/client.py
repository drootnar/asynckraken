import aiohttp
import async_timeout
from urllib import parse
from typing import Dict

from . import version
from .types import ApiMethod, ApiConfig
from .auth import KrakenHMAC


class ErrorResponse(Exception):
    pass


class Client(object):
    def __init__(
        self,
        key: str,
        secret: str,
        uri: str='https://api.kraken.com',
        timeout: int=30,
        session: aiohttp.ClientSession=None
    ) -> None:
        self.api = ApiConfig(
            key=key,
            secret=secret,
            uri=uri,
            version='0'
        )
        self.headers = {
            'User-Agent': 'asynckraken/' + version.__version__ +
            ' (+' + version.__url__ + ')'
        }
        self.timeout = timeout
        self.session = session if session else aiohttp.ClientSession()

    async def query_public(
        self,
        method: str,
        params: Dict=None
    ) -> Dict:
        urlpath = '/' + self.api.version + '/public/' + method
        if params is None:
            params = {}
        return await self._query(ApiMethod.public, urlpath, params)

    async def query_private(
        self,
        method: str,
        params: Dict=None
    ) -> Dict:
        urlpath = '/' + self.api.version + '/private/' + method
        if params is None:
            params = {}
        auth = KrakenHMAC(params, urlpath, self.api)
        params['nonce'] = auth.nonce
        headers = auth.headers
        return await self._query(ApiMethod.private, urlpath, params, headers)

    async def _query(
        self,
        method: str,
        urlpath: str,
        params: Dict,
        headers: Dict=None
    ) -> Dict:
        url = self.api.uri + urlpath
        if headers is None:
            headers = {}
        headers.update(self.headers)
        if method == ApiMethod.private:
            data = parse.urlencode(params)
            params = None
        else:
            data = None
        with async_timeout.timeout(self.timeout):
            async with getattr(self.session, method)(
                url,
                data=data,
                params=params,
                headers=headers
            ) as response:
                result = await response.json()

        if response.status not in (200, 201, 202):
            raise ErrorResponse

        return result
