#!/usr/bin/env python3

"""
Mail sender client
See:
    https://github.com/Anthony25/mail-sender-client
"""

from setuptools import setup, find_packages

setup(
    name="mail-sender-client",
    version="0.0.1",

    description="Mail sender with automatic failover",

    url="https://github.com/Anthony25/mail-sender-client",
    author="Anthony25 <Anthony Ruhier>",
    author_email="anthony.ruhier@gmail.com",

    license="Simplified BSD",

    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
    ],

    keywords="mail",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["argparse", "requests"],
    entry_points={
        'console_scripts': [
            'mail-sender-client = mail_sender_client.__main__:parse_args',
        ],
    }
)
