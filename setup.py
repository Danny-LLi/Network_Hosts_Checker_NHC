#!/usr/bin/env python3
from setuptools import setup
from setuptools.command.install import install






setup(
    name='nhc',
    version='1.0.0',
    scripts=['nhc.py'],
    py_modules=['nhc'],
    description='Network_Hosts_Checker_NHC is a powerfull tool to check your network hosts',
    long_description= 'README.md',
    author='Danny LLi',
    author_email='dannylligithub@gmail.com',
    url='https://github.com/Danny-LLi/Network_Hosts_Checker_NHC',
    install_requires=[
#        'scapy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'nhc=nhc:main'
        ]
    }
)


