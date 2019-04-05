#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:15:13 2019

@author: egmm
"""

import os
import sys
import setuptools
from distutils.util import convert_path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.append(os.getcwd())

main_ = {}
ver_path = convert_path('pypep/__init__.py')
with open(ver_path) as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, main_)

setup(
    name='pypep',
    description = 'A Petroeleum Engineering Project based on Python',
    version=main_['__version__'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Petroleum'
    ],
    packages = setuptools.find_packages(),
    install_requires=[
        'numpy>=1.15',
        'scipy>=1.1',
        'matplotlib',
        'pandas'
        ],
    author='Edgar G. Martinez',
    author_email='edgarg.martinezm@gmail.com',
    download_url='https://github.com/edgargmartinez/PyPEP/'
)