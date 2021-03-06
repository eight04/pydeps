#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""pydeps - Python module dependency visualization
"""
# pragma: nocover
import setuptools
from distutils.core import setup
from setuptools.command.test import test as TestCommand

version='1.4.0'


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

    
setup(
    name='pydeps',
    version=version,
    packages=['pydeps'],
    install_requires=[
        'enum34',
        'stdlib_list',
    ],
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': [
            'pydeps = pydeps.pydeps:pydeps',
        ]
    },
    url='https://github.com/thebjorn/pydeps',
    license='BSD',
    author='bjorn',
    author_email='bp@datakortet.no',
    description='Display module dependencies',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
