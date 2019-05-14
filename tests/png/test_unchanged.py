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
from . import RESOURCES_PATH
from io import SEEK_SET
from sevensource.formats.png import PNG
from sevensource.formats.png.plugin import ChunkStatus

image_path = os.path.join(RESOURCES_PATH, 'unchanged.png')

HEADER_LEN = 8
CHUNK_START = HEADER_LEN


def test_header_pos():
    with open(image_path, 'rb') as f:
        plugin = PNG('', '')
        res = plugin._find_header(f)
        assert (res == 0)

        res = plugin._find_header(f)
        assert (res is None)


def test_chunk_parsing():
    with open(image_path, 'rb') as f:
        f.seek(CHUNK_START, SEEK_SET)
        plugin = PNG('', '')

        while True:
            res = plugin._parse_chunk(f)

            assert (res != ChunkStatus.ERROR)

            if res == ChunkStatus.END:
                break
