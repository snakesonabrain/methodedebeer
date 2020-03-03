#!/usr/bin/env python3

import os
from setuptools import setup, find_packages
from debeer.__version__ import __version__
# load the README file and use it as the long_description for PyPI
def readme():
    with open('README.md', 'r') as f:
        readme = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(name='methodedebeer',
      version=__version__,
      description='methodedebeer, Ghent University open-source implementation of axial pile capacity calculations according to Belgian practice',
      long_description=readme(),
      url='https://github.com/snakesonabrain/methodedebeer',
      download_url='https://github.com/snakesonabrain/methodedebeer/archive/master.zip',
      keywords=['engineering', 'geotechnical', 'piles'],
      author='Bruno Stuyts',
      author_email='bruno.stuyts@ugent.be',
      license='Creative Commons BY-SA 4.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],)