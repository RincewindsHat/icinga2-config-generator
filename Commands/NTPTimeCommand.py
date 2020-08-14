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


class NTPTimeCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id):
        ConfigBuilder.validate_id(id)
        command = ConfigBuilder.get_command(id)
        if None is command:
            id = 'command_' + id
            command = NTPTimeCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_ntp_time'

    def get_arguments(self):
        config = """{
    "--use-ipv4" = {
      value = "$command_ntp_time_force_ipv4$"
      set_if = "$command_ntp_time_force_ipv4$"
    }
    "--use-ipv6" = {
      value = "$command_ntp_time_force_ipv6$"
      set_if = "$command_ntp_time_force_ipv6$"
    }
    "--hostname" = {
      value = "$command_ntp_time_ntp_server$"
    }
    "--port" = {
      value = "$command_ntp_time_ntp_server_port$"
      set_if = "$command_ntp_time_ntp_server_port$"
    }
    "--quiet" = {
      set_if = "$command_ntp_time_quiet$"
    }
    "--warning" = {
      value = "$command_ntp_time_warning$"
    }
    "--critical" = {
      value = "$command_ntp_time_critical$"
    }
    "--time_offset" = {
      value = "$command_ntp_time_time_offset$"
      set_if = "$command_ntp_time_time_offset$"
    }
    "--delay" = {
      value = "$command_ntp_time_delay$"
      set_if = "$command_ntp_time_delay$"
    }
    "--stratum-warn" = {
      value = "$command_ntp_time_stratum_warn$"
      set_if = "$command_ntp_time_stratum_warn$"
    }
    "--stratum-crit" = {
      value = "$command_ntp_time_stratum_crit$"
      set_if = "$command_ntp_time_stratum_crit$"
    }
    "--timeout" = {
      value = "$command_ntp_time_timeout$"
      set_if = "$command_ntp_time_timeout$"
    }
  }
"""

        return config
