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
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class Webrequest(Check):

    def __init__(self, id: str, class_name: str, command_name: str, command_name_prefix: str):
        Check.__init__(self, id, class_name, f"{command_name_prefix}_{command_name}")
        self._command_name = command_name
        self.__header = None
        self.__uri = None
        self.__domain = None
        self.__port = None
        self.__ssl = False
        self.__client_cert = None
        self.__client_key = None
        self.add_service_group(ServiceGroup.create('webserver'))

    def set_header(self, header):
        ValueChecker.is_string(header)
        if None is self.__header:
            self.__header = []
        self.__header.append(header)
        return self

    def get_header(self):
        return self.__header

    def set_uri(self, uri):
        ValueChecker.is_string(uri)
        self.__uri = uri
        return self

    def get_uri(self):
        return self.__uri

    def set_domain(self, domain):
        ValueChecker.is_string(domain)
        self.__domain = domain
        return self

    def get_domain(self):
        return self.__domain

    def set_port(self, port):
        ValueChecker.is_number(port)
        self.__port = port
        return self

    def get_port(self):
        return self.__port

    def set_ssl(self, ssl):
        ValueChecker.is_bool(ssl)
        self.__ssl = ssl
        return self

    def get_ssl(self):
        return self.__ssl

    def set_client_cert(self, client_cert):
        ValueChecker.is_string(client_cert)
        self.__client_cert = client_cert
        return self

    def get_client_cert(self):
        return self.__client_cert

    def set_client_key(self, client_key):
        ValueChecker.is_string(client_key)
        self.__client_key = client_key
        return self

    def get_client_key(self):
        return self.__client_key

    def get_custom_config(self) -> str:
        return ValueMapper.get_property_default_config(self, 'Webrequest', self._command_name, 'command')

    def get_config(self) -> str:
        self.validate()
        Webrequest.validate(self)
        config = Check.get_config(self)
        return config

    def validate(self):
        pass
