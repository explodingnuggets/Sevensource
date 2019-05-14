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
import os
import zlib
from enum import Enum
from sevensource.plugins import FormatProvider
from sevensource.files.file import FileOperations


class ChunkStatus(Enum):
    OK = 0
    END = 1
    ERROR = 2


class PNG(FormatProvider):
    name = 'PNG'
    extension = 'png'

    ''' PNG format specifics '''
    __BYTE_ORDER = 'big'
    __HEADER = b'\x89PNG\x0d\x0a\x1a\x0a'
    __HEADER_LEN = len(__HEADER)
    __TYPE_IEND = 'IEND'
    __CRITICAL_TYPES = ['IHDR', 'IDAT', 'PLTE', __TYPE_IEND]

    def _find_header(self, f: io.BufferedReader) -> int:
        while True:
            bytes_read = f.read(self.__HEADER_LEN)

            if len(bytes_read) != self.__HEADER_LEN:
                return

            if bytes_read == self.__HEADER:
                return f.tell() - self.__HEADER_LEN

            f.seek(-(self.__HEADER_LEN - 1), io.SEEK_CUR)

    def _read_chunk(self, f: io.BufferedReader) -> tuple:
        chunk_len = f.read(4)
        chunk_leni = int.from_bytes(chunk_len, self.__BYTE_ORDER)
        chunk_rest = f.read(8 + chunk_leni)

        if len(chunk_rest) == 8 + chunk_leni:
            chunk_typ = chunk_rest[:4]
            chunk_dat = chunk_rest[4:4 + chunk_leni]
            chunk_crc = chunk_rest[4 + chunk_leni:]

            return (chunk_len, chunk_typ, chunk_dat, chunk_crc)

    def _check_chunk_type(self, chunk_type: str) -> bool:
        if chunk_type[0].isupper() and chunk_type in self.__CRITICAL_TYPES:
            return True
        elif chunk_type.isalpha() and chunk_type[2].isupper():
            return True

        return False

    def _check_chunk_crc(self, chunk: bytes, chunk_crc: int) -> bool:
        crc = zlib.crc32(chunk)

        return (crc == chunk_crc)

    def _parse_chunk(self, f: io.BufferedReader) -> ChunkStatus:
        chunk_read = self._read_chunk(f)

        if chunk_read is not None:
            chunk_len, chunk_typ, chunk_dat, chunk_crc = chunk_read
            chunk = chunk_typ + chunk_dat
            chunk_leni = int.from_bytes(chunk_len, self.__BYTE_ORDER)
            chunk_typs = chunk_typ.decode('utf-8')
            chunk_crci = int.from_bytes(chunk_crc, self.__BYTE_ORDER)

            if (self._check_chunk_type(chunk_typs) and
                    self._check_chunk_crc(chunk, chunk_crci)):

                if chunk_typs == self.__TYPE_IEND:
                    return ChunkStatus.END

                return ChunkStatus.OK

            f.seek(-(12 + chunk_leni), io.SEEK_CUR)

        return ChunkStatus.ERROR

    def _get_file_path(self, index: int) -> str:
        filename = f'image-{index}.{self.extension}'
        return os.path.join(self.out_path, filename)

    def execute(self):
        with open(self.in_path, 'rb') as f:
            index = 0

            while True:
                start_at = self._find_header(f)

                if start_at is None:
                    break

                while True:
                    chunk_status = self._parse_chunk(f)

                    if chunk_status == ChunkStatus.ERROR:
                        break

                    if chunk_status == ChunkStatus.END:
                        end_at = f.tell()
                        out_path = self._get_file_path(index)
                        FileOperations.copy(f, out_path, start_at, end_at)
                        index += 1
                        break
