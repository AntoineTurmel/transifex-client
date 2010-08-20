#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from codecs import BOM

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py

VERSION = '0.1'

readme_file = open(u'README')
long_description = readme_file.read()
readme_file.close()
if long_description.startswith(BOM):
    long_description = long_description.lstrip(BOM)
long_description = long_description.decode('utf-8')

package_data = {
    '': ['LICENSE', 'README'],
}

scripts = ['tx'] 

setup(
    name="tx",
    version=VERSION,
    scripts=scripts,
    description="A command line interface for Transifex",
    long_description=long_description,
    author="Indifex Ltd.",
    author_email="info@indifex.com",
    url="http://www.indifex.com",
    license="GPLv2",
    dependency_links = [
        "http://atlee.ca/software/poster/",
    ],
    setup_requires = [
        "poster >= 0.4",
    ],
    install_requires = [
        "poster >= 0.4",
    ],
    data_files=[
    ],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data = package_data,
    keywords = (
        'translation localization internationalization vcs',),
)
