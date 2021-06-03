# -*- coding: utf-8 -*-
#
# Copyright © Sacher-tec-500 Project Contributors
# Licensed under the terms of the GNU GPLv3+ License
# (see sacher-tec-500/__init__.py for details)

"""
Sacher-Tec-500
================
Python bindings for Sacher-Tec-500 DLLs. 
"""

import io
import sys

import setuptools

import sacher_tec as st

# ==============================================================================
# Constants
# ==============================================================================
NAME = "sacher-tec-500"
LIBNAME = "sacher-tec-500"

# ==============================================================================
# Use README for long description
# ==============================================================================
with io.open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# ==============================================================================
# Setup arguments
# ==============================================================================
setup_args = dict(
    name=NAME,
    version=st.__version__,
    author="Ertugrul Karademir",
    author_email="ekarademir@gmail.com",
    maintainer="Sequoia Ploeg",
    maintainer_email="sequoia.ploeg@ieee.org",
    url="https://github.com/BYUCamachoLab/thorlabs-kinesis",
    description="Python bindings to Thorlabs Kinesis API.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    # download_url=__website_url__ + "",
    license="GPLv3+",
    keywords="laboratory instrumentation hardware science motion control ThorLabs",
    platforms=["Windows",],
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.6",
)

setuptools.setup(**setup_args)