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
from sevensource.plugins import FormatProvider


class PNG(FormatProvider):
    name = 'PNG'

    ''' PNG format specifics '''
    __HEADER = b'\x89PNG\x0d\x0a\x1a\x0a'
    __HEADER_LEN = len(__HEADER)

    def __find_header(self, f: io.BufferedReader) -> int:
        while True:
            bytes_read = f.read(self.__HEADER_LEN)

            if len(bytes_read) != self.__HEADER_LEN:
                return

            if bytes_read == self.__HEADER:
                return f.tell() - self.__HEADER_LEN

            f.seek(-(self.__HEADER_LEN - 1), io.SEEK_CUR)

    def execute(self):
        with open(self.in_path, 'rb') as f:
            start_at = self.__find_header(f)

            if start_at is not None:
                pass
