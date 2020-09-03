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

from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class Zone:

    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    @staticmethod
    def create(id):
        ValueChecker.validate_id(id)

        zone = ConfigBuilder.get_zone(id)
        if None is zone:
            id = 'zone_' + id
            zone = Zone(id)
            ConfigBuilder.add_zone(id, zone)

        return zone

    def get_config(self):
        return ''