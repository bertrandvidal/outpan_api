#!/usr/bin/env python
import os
from setuptools import setup


README_PATH = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(README_PATH, "r") as readme_file:
    README = readme_file.read()


setup(
    name="outpan",
    version="1.0.1",
    description="Easily use Outpan API to get product info from its barcode",
    long_description=README,
    py_modules=["outpan"],
    author="Bertrand Vidal",
    author_email="vidal.bertrand@gmail.com",
    download_url="https://pypi.python.org/pypi/outpan",
    url="https://github.com/bertrandvidal/outpan_api",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "requests",
        "parse_this>=1.0.3",
    ],
)
