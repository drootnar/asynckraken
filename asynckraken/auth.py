import hashlib
import hmac
import base64
import time
from urllib import parse
from typing import Dict

from .types import ApiConfig


class KrakenHMAC(object):

    def __init__(
        self,
        params: Dict,
        urlpath: str,
        api_config: ApiConfig
    ) -> None:
        self.params = params
        self.urlpath = urlpath
        self.api_config = api_config
        self._nonce = self._generate_nonce()
        self._signature = self._calculate_signature()

    @property
    def nonce(self) -> int:
        return self._nonce

    @property
    def signature(self) -> str:
        return self._signature

    @property
    def headers(self) -> Dict:
        return {
            'API-Key': self.api_config.key,
            'API-Sign': self.signature,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def _calculate_signature(self) -> str:
        self.params['nonce'] = self._nonce
        postdata = parse.urlencode(self.params)
        encoded = (str(self._nonce) + postdata).encode()
        message = self.urlpath.encode() + hashlib.sha256(encoded).digest()
        signature = hmac.new(
            base64.b64decode(self.api_config.secret),
            message,
            hashlib.sha512
        )
        sigdigest = base64.b64encode(signature.digest())
        return sigdigest.decode()

    def _generate_nonce(self) -> int:
        return int(1000 * time.time())
