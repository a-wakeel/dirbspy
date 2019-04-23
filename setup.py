"""
Setuptools configuration file.

MIT License

Copyright (c) 2019 Abdul Wakeel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This file based on the example from the PyPA sample project, whose copyright is
included below:
Copyright (c) 2016 The Python Packaging Authority (PyPA)
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
import re
import sys

here = path.abspath(path.dirname(__file__))

if sys.version_info[0] != 3:
    sys.exit('Only Python 3.x supported')

# get long description of the package
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Version snippet from the following URL:
# https://github.com/pypa/python-packaging-user-guide/blob/master/source/single_source_version.rst
#
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license: http://creativecommons.org/licenses/by-sa/3.0
#


def read(*names):
    """Method to read file and return ref."""
    with open(path.join(here, *names), encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_path):
    """Method to find version str from file."""
    version_file = read(*file_path)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)

    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='dirbspy',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=find_version("src/dirbspy", "__init__.py"),
    description='A friendly Python API interface for Device Identification Registration & Blocking System (DIRBS)',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/a-wakeel/dirbspy',
    license='MIT',

    # Author details
    author='Abdul Wakeel',
    author_email='awkhan978@gmail.com',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages('src'),
    package_dir={'': 'src'},

    # place packages here
    install_requires=[],
)
