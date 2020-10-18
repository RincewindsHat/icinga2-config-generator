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

from Commands.Command import Command
from ConfigBuilder import ConfigBuilder
from ValueChecker import ValueChecker


class UptimeCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
            command = UptimeCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_uptime'

    def get_arguments(self):
        config = """{
    "--warning" = {
      value = "$command_uptime_warning$"
    }
    "--critical" = {
      value = "$command_uptime_critical$"
    }
    "--for" = {
      value = "$command_uptime_for$"
      set_if = {{ macro("$command_uptime_for$") != false }}
    }
    "--since" = {
      value = "$command_uptime_since$"
      set_if = {{ macro("$command_uptime_since$") != false }}
    }
  }
"""

        return config
