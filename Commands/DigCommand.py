#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de> https://f-froehlich.de
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


class DigCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id):
        ConfigBuilder.validate_id(id)
        command = ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
            command = DigCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_dig'

    def get_arguments(self):
        config = """{
    "--hostname" = {
      value = "$command_dig_dnsserver_hostname$"
      set_if = "$command_dig_dnsserver_hostname$"
    }
    "--port" = {
      value = "$command_dig_dnsserver_port$"
      set_if = "$command_dig_dnsserver_port$"
    }
    "--use-ipv4" = {
      value = "$command_dig_only_ipv4$"
      set_if = "$command_dig_only_ipv4$"
    }
    "--use-ipv6" = {
      value = "$command_dig_only_ipv6$"
      set_if = "$command_dig_0nly_ipv6$"
    }
    "--query_address" = {
      value = "$command_dig_question$"
    }
    "--record_type" = {
      value = "$command_dig_record_type$"
    }
    "--expected_address" = {
      value = "$command_dig_expected_address$"
    }
    "--dig-arguments" = {
      value = "$command_dig_question_arguments$"
      set_if = "$command_dig_question_arguments$"
    }
    "--timeout" = {
      value = "$command_dig_timeout$"
    }
    "--warning" = {
      value = "$command_dig_warning_time$"
    }
    "--critical" = {
      value = "$command_dig_critical_time$"
    }
  }
"""

        return config
