#!/usr/bin/env python
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), "r") as readme_file:
    readme = readme_file.read()

setup(
    name = "outpan",
    version = "0.1.4",
    description = "Easily use Outpan.com API to get product info from their barcode",
    long_description = readme,
    py_modules = ["outpan"],
    author = "Bertrand Vidal",
    author_email = "vidal.bertrand@gmail.com",
    download_url = "https://pypi.python.org/pypi/outpan",
    url = "https://github.com/bertrandvidal/outpan_api",
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires = [
        "requests",
        "parse_this>=0.4.0",
    ],
)
