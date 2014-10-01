#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


readme = open('README.rst').read()


setup(
    name='wsgiappversion',
    version='0.0.1',
    description="Wsgi middleware that exposes an app's version number",
    long_description=readme,
    author='Rob Berry',
    author_email='rob@lostpropertyhq.com',
    url='https://github.com/LostProperty/wsgiappversion',
    packages=[
        'wsgiappversion',
    ],
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    keywords='wsgi version',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
