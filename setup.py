# -*- coding: utf-8 -*-
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved.

""" setup.py for cp4s-sdk Python Module """

from setuptools import setup, find_packages
setup(
    name="cp4s_sdk",
    version="1.0.0",
    license="MIT",
    packages=find_packages(),

    # Installation Dependencies
    setup_requires=[],

    # Runtime Dependencies
    install_requires=[
        'cp4s-connector-sdk @ git+https://github.com/Ryan-Gordon1/cp4s-connector-sdk.git',
        'resilient_sdk'
    ],
    dependency_links=[
        "git+https://github.com/Ryan-Gordon1/cp4s-connector-sdk.git#egg=cp4s-connector-sdk"
    ],
    # Add command line: cp4s-sdk
    entry_points={
        "console_scripts": ["cp4s-sdk=cp4s_sdk.sdk:main"]
    },

    # PyPI metadata
    author="Ryan Gordon",
    author_email="ryan.gordon1@ibm.com",
    description="Python SDK for developing Extensions or Apps for any product under the Cloud Pak for Security Ecosystem",
    url="https://github.com/Ryan-Gordon1/cp4s-sdk",
    project_urls={
        "IBM Community": "http://ibm.biz/soarcommunity",
        "GitHub": "https://github.com/Ryan-Gordon1/cp4s-sdk"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="ibm cloud pak cp4s cases qradar qapp circuits sdk resilient-sdk",
)
