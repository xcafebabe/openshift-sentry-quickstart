# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='sentry_now',
    version='0.1',
    description='Sentry instance based on Python-2.7 Community Cartridge',
    author=u'José Moreira, Joao Oliveira',
    AuthorO_email='joaoxsouls@gmail.com',
    url='https://github.com/getsentry/sentry/',
    install_requires=[
        'sentry==8.7.0',
        'psycopg2==2.6.0',
        'flake8'
    ],
)
