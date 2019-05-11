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

import sys
from .commands import parse_args
from .formats import *
from .plugins import FormatProvider


def main():
    args = parse_args()

    in_path = args.input
    out_path = args.output
    buffer_size = args.buffersize

    for p in FormatProvider.get_plugins(in_path, out_path, buffer_size):
        p.execute()

if __name__ == '__main__':
    main()
