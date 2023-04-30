#!/usr/bin/python3
# -*- coding: utf-8
from __future__ import annotations

from typing import List

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.MailNotificationCommand import MailNotificationCommand
from icinga2confgen.Notification.Notification import Notification
from icinga2confgen.User.User import User
from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


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


class MailNotification(Notification):

    @staticmethod
    def create(id: str, force_create: bool = False) -> MailNotification:
        ValueChecker.validate_id(id)

        notification = None if force_create else ConfigBuilder.get_notification(id)
        if None is notification:
            notification = MailNotification(id)
            ConfigBuilder.add_notification(id, notification)

        return notification

    def get_command_config(self) -> MailNotificationCommand:
        return MailNotificationCommand.create('mail')

    def user_config_function(self, user: User) -> List[str]:
        email_config = []
        for email in user.get_email():
            email_config.append(ValueMapper.parse_var('vars.notification_email', email))
        return email_config

    def group_config_function(self, group: UserGroup) -> List[str]:
        email_config = []
        for email in group.get_email():
            email_config.append(ValueMapper.parse_var('vars.notification_email', email))
        return email_config
