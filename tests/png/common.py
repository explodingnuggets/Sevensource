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

import io
from sevensource.formats.png import PNG
from sevensource.formats.png.plugin import ChunkStatus


def assert_find_header(f: io.BufferedReader, exp: int):
    plugin = PNG('', '')
    res = plugin._find_header(f)

    assert (res == exp)


def assert_parse_chunk(f: io.BufferedReader):
    plugin = PNG('', '')

    while True:
        res = plugin._parse_chunk(f)

        assert (res != ChunkStatus.ERROR)

        if res == ChunkStatus.END:
            break
