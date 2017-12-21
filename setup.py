import pypandoc

from setuptools import setup
from codecs import open
from os import path

#converts markdown to reStructured
converter_readme = pypandoc.convert('README.md', 'rst', format='markdown')

#writes converted file
with open('README.rst', 'w') as outfile:
    outfile.write(converter_readme)

# Get the long description from the README file
with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='jsonconfigreader',
      version='1.0.1',
      description='Python JSON configuration reader and parser',
      long_description=long_description,
      author='Andrei Surzhan',
      author_email='surzhan.a.y@gmail.com',
      url='https://github.com/AndreySurzhan/jsonconfigparser',
      packages=['jsonconfigreader'],
      classifiers=[
          'Topic :: Utilities',
          'Intended Audience :: Developers',
          'Intended Audience :: Other Audience',
          'Operating System :: Microsoft :: Windows :: Windows 10',
          'Operating System :: MacOS',
          'Operating System :: Unix',
          'Programming Language :: Python'
          ]
      )
