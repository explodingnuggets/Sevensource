# Copyrights and license
#
# Sevensource: a file recovery tool
# Copyright (C) 2019 Matheus Bortoleto da Silva <matheus.silvaufscar@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or any
# later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from src.sevensource.__meta__ import __author__, __version__

setup(
    name='sevensource',
    version=__version__,
    author=__author__,
    author_email='matheus.silvaufscar@gmail.com',
    description='A file recovery tool',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 :: Alpha',
        'License :: OSI Approved :: GNU GPL 3.0',
        'Programming Language :: Python :: 3'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[],
    extras_require={
        'dev': [
            'pep8',
            'pylint',
            'pytest',
            'tox'
        ]
    },
    entry_points={
        'console_scripts': [
            'sevensource=sevensource.app:main'
        ]
    }
)
