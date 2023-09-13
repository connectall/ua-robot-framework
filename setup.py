#!/usr/bin/env python

import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 1 - Development/Unstable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3 :: Only
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()

with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name             = 'robot-connectall',
    version          = '0.0.1',
    description      = 'ConnectALL library for Robot Framework',
    long_description = 'ConnectALL library for Robot Framework',
    author           = 'Sharath Bhaskara',
    author_email     = 'sharath.bhaskara@broadcom.com',
    url              = 'https://github.com/connectall/robotframework-connectall-library',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework testexecution testing connectall reporting',
    platforms        = 'any',
    classifiers      = CLASSIFIERS,
    python_requires  = '>=3.6, <4',
    install_requires = REQUIREMENTS,
    package_dir      = {'': 'ConnectAllLibrary'},
    packages         = find_packages('ConnectAllLibrary'),
    py_modules       = ['ConnectAllListener', 'RestClient', 'BasicAuthRestClient'],
    package_data     ={
        'ConnectAllLibrary':
            ['*.pyi']
    }
)
