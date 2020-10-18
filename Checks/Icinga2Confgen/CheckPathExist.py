#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@icinga2.confgen.org> https://icinga2.confgen.org
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  For all license terms see README.md and LICENSE Files in root directory of this Project.

from Checks.Check import Check
from Commands.Icinga2Confgen.PathExistCommand import PathExistCommand
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class CheckPathExists(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckPathExists', 'path_exist')
        self.__file = None
        self.__dir = None
        self.__invert = False

    def set_file(self, file):
        ValueChecker.is_string(file)
        self.__file = file
        return self

    def get_file(self):
        return self.__file
    
    def set_dir(self, dir):
        ValueChecker.is_string(dir)
        self.__dir = dir
        return self

    def get_dir(self):
        return self.__dir

    def set_invert(self, invert):
        ValueChecker.is_bool(invert)
        self.__invert = invert
        return self

    def get_invert(self):
        return self.__invert


    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            id = 'check_' + id
            check = CheckPathExists(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('path_exist'):
            PathExistCommand.create('path_exist')

        return check
