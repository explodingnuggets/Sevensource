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


class PluginMount(type):
    '''
        Metaclass for plugins, being a central mounting point for any
        implemented plugin
    '''
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)

    def get_plugins(cls, *args, **kwargs):
        return [p(*args, **kwargs) for p in cls.plugins]


class FormatProvider(metaclass=PluginMount):
    '''
        Mount point for plugins which refer to file formats that can be
        recovered

        Plugins implementing this interface should have these attributes

        --------    ----------------------------------------------------
        name        The name of the file format implemented

        in_path     The input path, which can be a file or device

        out_path    The output path, where found files will be saved
        --------    ----------------------------------------------------
    '''
    def __init__(self, in_path, out_path):
        self.in_path = in_path
        self.out_path = out_path
