#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

setup(name='configure',
      version='0.0.2',
      description='Python Configure Utility',
      author='Keith Lee',
      author_email='code@keithlee.co.uk',
      url='https://github.com/keithlee-co-uk/configure',
      dependency_links=['git+https://github.com/keithlee-co-uk/dbconnection.git#egg=dbconnection'],

      install_requires=['configobj',
                        'Crypto',
                        'dbconnection'],
      extras_require={
          'test': ["pytest"],
      }
      )
