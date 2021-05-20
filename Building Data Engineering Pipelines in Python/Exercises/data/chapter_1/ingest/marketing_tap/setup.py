#!/usr/bin/env python

from setuptools import setup

setup(name='tap-marketing-api',
      version='0.0.1',
      description="Singer tap for pulling all data from my company's internal marketing API",
      author='DataCamp Student',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_marketing_api'],
      install_requires=[
          'requests>=2.21.0',
          'singer-python>=2.1.4',
      ],
      entry_points='''
          [console_scripts]
          tap-marketing-api=tap_marketing_api:main
      ''',
      )
