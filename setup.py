from pathlib import Path

from setuptools import setup, Command


class GenerateReadMeRst(Command):
    description = "Generate README.rst out of README.md"

    user_options = [
        ('genreadme', None, None),
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Function that generates README.rst out of README.md

        :return: void
        """
        try:
            import pypandoc
        except ImportError:
            print("Install pypandoc to generate README.rst")
            pypandoc = None
        if pypandoc:
            pypandoc.convert_file('README.md', 'rst', outputfile='README.rst')


my_file = Path('README.rst')
if my_file.is_file():
    long_description = my_file.read_text()
else:
    long_description = 'README doesn\'t exist'

setup(name='jsonconfigreader',
      cmdclass={
          'genreadme': GenerateReadMeRst,
      },
      version='1.3.1',
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
