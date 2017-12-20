#!/usr/bin/env python

from setuptools import setup
from codecs import open
from os import path

# Get the long description from the README file
with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='jsonconfigparser',
      version='1.0',
      description='Python JSON configuration parser',
      long_description=long_description,
      author='Andrei Surzhan',
      author_email='surzhan.a.y@gmail.com',
      url='', #should be home url of the project once we have pypi server installed
      packages=['jsonconfigparser'],
      classifiers=[
          'Topic :: Utilities',
          'Intended Audience :: QAs :: Devs',
          'Operating System :: Microsoft :: Windows :: Windows 10',
          'Programming Language :: Python'
          ]
      )
