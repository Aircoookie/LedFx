#!/usr/bin/env python3

from datetime import datetime as dt
from setuptools import setup, find_packages
import ledfxcontroller.consts as const

PROJECT_PACKAGE_NAME = 'ledfxcontroller'
PROJECT_VERSION = const.PROJECT_VERSION
PROJECT_LICENSE = 'The MIT License'
PROJECT_AUTHOR = 'Austin Hodges'
PROJECT_AUTHOR_EMAIL = 'austin.b.hodges@gmail.com'
PROJECT_URL = 'http://github.com/ahodges9/ledfx'

REQUIRES = [
    'numpy==1.13.3',
    'scipy>=0.15.1',
    'voluptuous==0.11.1',
    'pyaudio==0.2.11',
    'sacn==1.3',
    'aiohttp==3.3.2',
    'aiohttp_jinja2==1.0.0',
    'pyyaml>=3.11,<4'
]

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    license = PROJECT_LICENSE,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_AUTHOR_EMAIL,
    url=PROJECT_URL,
    install_requires=REQUIRES,
    python_requires=const.REQUIRED_PYTHON_STRING,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ledfx = ledfxcontroller.__main__:main'
        ]
    }
)
