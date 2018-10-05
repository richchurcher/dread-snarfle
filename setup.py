#!/usr/bin/env python
import setuptools

version = '0.1.0'

install_requires = ()

setuptools.setup(
    name='dread_snarfle',
    version=version,
    author='Rich Churcher',
    author_email='rich.churcher@gmail.com',
    url='https://github.com/richchurcher/dread-snarfle',
    packages=['dread_snarfle'],
    install_requires=install_requires,
    setup_requires=['pytest-runner'],

    extras_require={
        'test': (
            'asynctest',
            'pytest > 3.3.2',
            'pytest-aiohttp',
            'pytest-asyncio',
        ),
        'dev': (
            'flake8',
            'flake8-commas',
            'flake8-isort',
            'flake8-mypy',
            'flake8-quotes',
            'pytest-cov',
        ),
    },
)