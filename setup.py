from setuptools import setup, find_packages

version = '0.1.8'
description = 'A Python library for interacting with the Apex Legends Live API.'
long_description = 'A Python library for interacting with the Apex Legends Live API. Includes recieving game events and sending events to interact with the game.'

setup(
    name='LiveApex',
    version=version,
    author='Catotron',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'protobuf==6.30.1',
        'websockets==12.0'
    ],

    keywords='apex legends, live api, python, library',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6'
)