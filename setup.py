__author__ = 'aelkikhia'

# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='pyduels_engine',
    version='0.1',
    description='Duels engine written in python',
    author='Taz El-Kikhia',
    author_email='aelkikhia@gmail.com',
    tests_require=[
        "pep8",
        "mock",
        "nose",
        "nosexcover",
        "testtools"
    ],
    install_requires=[
    ],
    test_suite='nose.collector',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)
