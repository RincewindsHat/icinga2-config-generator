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
from Commands.Icinga2Confgen.DenyTlsVersionCommand import DenyTlsVersionCommand
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class CheckDenyTlsVersion(Check):

    def __init__(self, id):
        Check.__init__(self, id, 'CheckDenyTlsVersion', 'deny_tls_version')
        self.__protocol = None
        self.__domain = None
        self.__address = None

    def set_protocol(self, number):
        ValueChecker.is_string(number)
        self.__protocol = number
        return self

    def get_protocol(self):
        return self.__protocol

    def set_address(self, address):
        ValueChecker.is_string(address)
        self.__address = address
        return self

    def get_address(self):
        return self.__address

    def set_domain(self, number):
        ValueChecker.is_string(number)
        self.__domain = number
        return self

    def get_domain(self):
        return self.__domain

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)
        check = ConfigBuilder.get_check(id)
        if None is check:
            id = 'check_' + id
            check = CheckDenyTlsVersion(id)
            ConfigBuilder.add_check(id, check)

        if None is ConfigBuilder.get_command('deny_tls_version'):
            DenyTlsVersionCommand.create('deny_tls_version')

        return check
