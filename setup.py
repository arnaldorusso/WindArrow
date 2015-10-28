#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = open('history.md').read().replace('.. :changelog:', '')

setup(
    name='WindArrow',
    version='0.1.0',
    description='Plot Wind Arrow 2D plot - length based on wind intensity and angle based in wind direction.',
    long_description=readme + '\n\n' + history,
    author='Arnaldo Russo',
    author_email='arnaldorusso@gmail.com',
    url='https://github.com/arnaldorusso/WindArrow',
    packages=[
        'WindArrow',
    ],
    # package_dir={'': 'src'},
    #include_package_data=True,
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    license="MIT License",
    zip_safe=False,
    keywords='Wind plot arrow',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Oceanography',
    ],
    test_suite='tests',
)
