#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from cf_iso import __version__


def readme():
    '''
    Returns the contents of the README file as a string
    '''
    with open('README.rst') as f:
        return f.read()

reqs = [line.strip() for line in open('requirements.txt')]
test_reqs = [line.strip() for line in open('dev-requirements.txt')]

setup(
    name='cf-iso',
    version=__version__,
    description='Create ISO Metadata from CF Metadata',
    packages=find_packages(exclude=['tests', 'test.*']),
    long_description=readme(),
    author='Luke Campbell',
    author_email='luke.s.campbell@gmail.com',
    url='https://github.com/lukecampbell/cf-iso/',
    install_requires=reqs,
    test_requires=test_reqs,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: GIS'
    ],
)
