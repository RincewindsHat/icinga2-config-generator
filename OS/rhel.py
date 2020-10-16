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
from OS.OS import OS
from PackageManager.PackageManager import rpm

os_rhel_1 = OS.create('rhel_1').set_distro('rhel').set_version('1').set_os('Red Hat Enterprise Linux 1').set_package_manager(rpm)
os_rhel_2 = OS.create('rhel_2').set_distro('rhel').set_version('2').set_os('Red Hat Enterprise Linux 2').set_package_manager(rpm)
os_rhel_3 = OS.create('rhel_3').set_distro('rhel').set_version('3').set_os('Red Hat Enterprise Linux 3').set_package_manager(rpm)
os_rhel_4 = OS.create('rhel_4').set_distro('rhel').set_version('4').set_os('Red Hat Enterprise Linux 4').set_package_manager(rpm)
os_rhel_5 = OS.create('rhel_5').set_distro('rhel').set_version('5').set_os('Red Hat Enterprise Linux 5').set_package_manager(rpm)
os_rhel_6 = OS.create('rhel_6').set_distro('rhel').set_version('6').set_os('Red Hat Enterprise Linux 6').set_package_manager(rpm)
os_rhel_7 = OS.create('rhel_7').set_distro('rhel').set_version('7').set_os('Red Hat Enterprise Linux 7').set_package_manager(rpm)
os_rhel_8 = OS.create('rhel_8').set_distro('rhel').set_version('8').set_os('Red Hat Enterprise Linux 8').set_package_manager(rpm)
