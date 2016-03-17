# -*- Mode: Python -*-
"""ping
"""
from setuptools import setup
from codecs import open
from os import path
import os

setup(
    name='ping',
    version=0.1,
    description='Pure python3 ping implementation',
    long_description="",
    url='https://github.com/21dotco/two1',
    author='Corentin Debains',
    author_email='corentone@hotmail.com',
    license='GNUGPLv2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU GPL v2',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='ping icmp',
)