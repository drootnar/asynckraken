# Installation

`pip install asynckraken`

PyPI package [https://pypi.python.org/pypi/asynckraken](https://pypi.python.org/pypi/asynckraken)

# Usage


```python
import aiohttp
import asyncio

from asynckraken import Client

async def main():
    client = Client(key='api_key', secret='api_secret')
    result_public = await client.query_public('Depth', {'pair': 'XETHZEUR'})
    print(result_public)
    result_private = await client.query_private('Balance')
    print(result_private)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Development

Run with async python console: `docker-compose run shell`

Tests: `docker-compose run tests`

Full tests with type checking: `docker-compose run full_tests`


# Attribution


Core code is licensed under LGPLv3. See ``LICENSE.txt``.

Thanks for veox for writting [https://github.com/veox/python3-krakenex](python3-krakenex). I was using that code as example.
