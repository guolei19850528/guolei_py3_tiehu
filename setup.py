#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="guolei-py3-tiehu",
    version="2.0.0",
    description="铁虎 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guolei19850528/guolei_py3_tiehu",
    author="guolei",
    author_email="174000902@qq.com",
    license="MIT",
    keywors=["铁虎", "tiehu"],
    packages=setuptools.find_packages('./'),
    install_requires=[
        "guolei-py3-requests",
        "addict",
        "retrying",
        "jsonschema",
    ],
    python_requires='>=3.0',
    zip_safe=False
)
