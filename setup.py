from setuptools import setup, find_packages

version = '0.1.0'
description = 'A Python library for interacting with the Apex Legends Live API.'

setup(
    name='LiveApex',
    version=version,
    author='Catotron',
    description=description,
    packages=find_packages(),
    install_requires=[
        'protobuf',
        'websockets'
    ],

    keywords='apex legends, live api, python, library',
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ]
)