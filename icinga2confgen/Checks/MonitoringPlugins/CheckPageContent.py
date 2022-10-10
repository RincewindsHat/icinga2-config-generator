#!/usr/bin/python3
# -*- coding: utf-8

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
from icinga2confgen.Checks.Check import Check
from icinga2confgen.Helpers.Webrequest import Webrequest
from icinga2confgen.Commands.MonitoringPlugins.PageContentCommand import PageContentCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckPageContent(Webrequest):

    def __init__(self, id: str):
        Webrequest.__init__(self, id, 'CheckPageContent', 'page_content', 'monitoring_plugins')
        self.__ok = None
        self.__warning = None
        self.__critical = None

    def set_ok(self, ok):
        ValueChecker.is_string(ok)
        if None is self.__ok:
            self.__ok = []
        self.__ok.append(ok)
        return self

    def get_ok(self):
        return self.__ok

    def set_warning(self, warning):
        ValueChecker.is_string(warning)
        if None is self.__warning:
            self.__warning = []
        self.__warning.append(warning)
        return self

    def get_warning(self):
        return self.__warning

    def set_critical(self, critical):
        ValueChecker.is_string(critical)
        if None is self.__critical:
            self.__critical = []
        self.__critical.append(critical)
        return self

    def get_critical(self):
        return self.__critical

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckPageContent(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckPageContent):
            raise Exception('Id must be for an instance of CheckPageContent but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_page_content'):
            PageContentCommand.create('monitoring_plugins_page_content')

        return check

    def validate(self):
        Webrequest.validate(self)

    def get_config(self) -> str:
        return Webrequest.get_config(self)

    def get_custom_config(self) -> str:
        # config = ValueMapper.parse_var('vars.allowed_ports', self.__allowed_ports)
        config = Webrequest.get_custom_config(self)

        return config