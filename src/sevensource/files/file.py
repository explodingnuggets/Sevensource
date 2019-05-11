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


class FileOperations():
    buffer_size = None

    @staticmethod
    def set_buffer_size(buffer_size: int):
        FileOperations.buffer_size = buffer_size

    @staticmethod
    def copy(f: io.BufferedReader, out_path: str, start: int, end: int):
        with open(out_path, 'wb') as out:
            f.seek(start, io.SEEK_SET)
            remaining_bytes = end - start

            while remaining_bytes > 0:
                read_num = min(FileOperations.buffer_size, remaining_bytes)
                out.write(f.read(read_num))
                remaining_bytes -= read_num

            f.seek(end, io.SEEK_SET)
