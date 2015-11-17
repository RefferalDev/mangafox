#!/usr/bin/env python

from distutils.core import setup

setup(name='mangafox',
    version='0.9.1.1',
    description='Mangafox manga spider. Download chapters easily.',
    author='Italo Maia',
    url='http://italomaia.com',
    install_requires=['lxml', 'werkzeug'],
    scripts=['mangafox.py'],
)
