from setuptools import setup


#converts markdown to reStructured
try:
    import pypandoc
except ImportError:
    print("Install pypandoc to generate the field long_description")
    pypandoc = None
if pypandoc:
    pypandoc.convert_file('README.md', 'rst', outputfile='README.rst')
    long_description = open('README.rst').read()
else:
    long_description = "[pypandoc missing]"

setup(name='jsonconfigreader',
      version='1.3.0',
      description='Python JSON configuration reader and parser',
      long_description=long_description,
      author='Andrei Surzhan',
      author_email='surzhan.a.y@gmail.com',
      url='https://github.com/AndreySurzhan/jsonconfigreader',
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
