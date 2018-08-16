#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='configure',
      version='0.0.1',
      description='Python Configure Utility',
      author='Keith Lee',
      author_email='code@keithlee.co.uk',
      url='https://github.com/keithlee-co-uk/configure',
      packages=['configure'],
      dependency_links=['http://github.com/ikeithlee-co-uk/dbconnection.git#egg=dbconnection'],

      install_requires=requirements,
      extras_require={
          'test': ["pytest"],
      }
      )
