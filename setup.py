#!/usr/bin/env python3

import os.path
from setuptools import setup, find_packages

exec(open('./asynckraken/version.py').read())

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='asynckraken',
    version=__version__,
    description='kraken.com cryptocurrency exchange API',
    long_description=read('README.md'),
    author='Kamil Rogalski',
    author_email='kamil.rogalski@pragmaticcoders.com',
    url=__url__,
    packages=find_packages(exclude=['docs', 'tests*']),
    dependency_links=[],
    classifiers=[
      'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'aiohttp>=2.2.0'
    ],
    setup_requires=[
        'pytest-runner==2.9'
    ],
    tests_require=[
        'pytest==3.0.4',
        'pytest-aiohttp==0.1.3',
        'pytest-mypy==0.3.0',
        'pytest-flakes==1.0.1',
        'pytest-pep8==1.0.6',
        'freezegun==0.3.8',
    ]
)
