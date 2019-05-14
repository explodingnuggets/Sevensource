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

import os
import pytest
from . import common, HEADER_LEN, RESOURCES_PATH
from io import SEEK_SET

IMAGE_PATH = os.path.join(RESOURCES_PATH, 'changed.png')

PADDING = 20
CHUNK_START = HEADER_LEN + PADDING


def test_header_pos():
    with open(IMAGE_PATH, 'rb') as f:
        common.assert_find_header(f, PADDING)
        common.assert_find_header(f, None)


def test_chunk_parser():
    with open(IMAGE_PATH, 'rb') as f:
        f.seek(CHUNK_START, SEEK_SET)

        common.assert_parse_chunk(f)
