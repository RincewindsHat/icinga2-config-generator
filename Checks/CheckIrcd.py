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
from Commands.IrcdCommand import IrcdCommand
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class CheckIrcd(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckIrcd', 'ircd')
        self.__host = None
        self.__warning = None
        self.__critical = None
        self.__port = None
        
    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host
        return self

    def get_host(self):
        return self.__host
        
    def set_warning(self, warning):
        ValueChecker.is_string(warning)
        self.__warning = warning
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_string(critical)
        self.__critical = critical
        return self

    def get_critical(self):
        return self.__critical

    def set_port(self, port):
        ValueChecker.is_string(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port


    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        check = ConfigBuilder.get_check(id)
        if None is check:
            id = 'check_' + id
            check = CheckIrcd(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('ircd'):
            IrcdCommand.create('ircd')

        return check