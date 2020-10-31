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


def get_default_group_name(id):
    default_names = {
        'amavisd': 'Amavisd',
        'antivirus': 'Antivirus',
        'apache': 'Apache',
        'apt': 'APT',
        'bind': 'Bind',
        'breeze': 'Breeze',
        'certificate_check': 'X.509 certificate',
        'clamd': 'Clamd',
        'containerd': 'Containerd',
        'cron': 'Cron',
        'database': 'Database',
        'deny_insecure_TLSv1_0_webserver': 'Deny insecure TLS 1.0 webserver',
        'deny_insecure_TLSv1_0_unchecked': 'Deny insecure TLS 1.0 unchecked',
        'deny_insecure_TLSv1_1_webserver': 'Deny insecure TLS 1.1 webserver',
        'deny_insecure_TLSv1_1_unchecked': 'Deny insecure TLS 1.1 unchecked',
        'deny_secure_TLSv1_2_webserver': 'Deny secure TLS 1.2 wevserver',
        'deny_secure_TLSv1_3_webserver': 'Deny secure TLS 1.3 wevserver',
        'dhcp': 'DHCP',
        'dig': 'dig',
        'disk': 'Disk',
        'dns': 'DNS',
        'dnssec': 'DNSSEC',
        'docker': 'Docker',
        'dovecot': 'Dovecot',
        'dummy': 'Dummy',
        'existing_user': 'Existing users',
        'file_age': 'File age',
        'firewall': 'Firewall',
        'flexlm': 'Flexlm',
        'freshclam': 'Freshclam',
        'ftp': 'FTP',
        'group_members': 'Group members',
        'hpjd': 'HP JD',
        'http_redirect': 'Http to https redirect',
        'http_redirect_unchecked': 'Http to https redirect unchecked',
        'icmp': 'ICMP',
        'ifstatus': 'Interface status',
        'imap': 'IMAP',
        'insecure_webserver': 'Insecure webserver',
        'insecure_TLSv1_0_Webserver': 'Insecure TLS v1.0 webserver',
        'insecure_TLSv1_1_Webserver': 'Insecure TLS v1.1 webserver',
        'ircd': 'IRCD',
        'jabber': 'Jabber',
        'ldap': 'LDAP',
        'load': 'Load',
        'log': 'Log',
        'mail': 'Mail',
        'mailq': 'Mail queue',
        'missing_http_redirect_check': 'Missing http to https redirect check',
        'mrt_gtraf': 'MRT graf',
        'mysql': 'MySQL',
        'network': 'Network',
        'nginx': 'NGINX',
        'nntp': 'NNTP',
        'no_certificate_check': 'No X.509 Certificate check',
        'ntp': 'NTP',
        'ns_client': 'NS Client',
        'opendkim': 'Open DKIM',
        'path_exists': 'Path exists',
        'php_fpm': 'PHP FPM',
        'postfix': 'Postfix',
        'postgres': 'PostgreSQL',
        'postgrey': 'Postgrey',
        'ping': 'Ping',
        'pop': 'POP',
        'procs': 'Procs',
        'radius': 'RADIUS',
        'rpc': 'RPC',
        'rsyslogd': 'Rsyslogd',
        'secure_webserver': 'Secure Webserver',
        'secure_TLSv1_2_unchecked': 'Secure TLS 1.2 unchecked',
        'secure_TLSv1_3_unchecked': 'Secure TLS 1.3 unchecked',
        'secure_TLSv1_2_webserver': 'Secure TLS 1.2 Webserver',
        'secure_TLSv1_3_webserver': 'Secure TLS 1.3 Webserver',
        'security': 'Security',
        'sensors': 'Sensors',
        'smart': 'SMART',
        'smtp': 'SMTP',
        'snmp': 'SNMP',
        'sshd': 'SSHD',
        'sshd_security': 'SSHD security',
        'sudoers': 'Sudoers',
        'swap': 'SWAP',
        'system_health': 'System health',
        'tcp': 'TCP',
        'tls': 'TLS',
        'tls_1_check': 'TLS v1.0 Check',
        'tls_1_1_check': 'TLS v1.1 Check',
        'tls_1_2_check': 'TLS v1.2 Check',
        'tls_1_3_check': 'TLS v1.3 Check',
        'tomcat': 'Apache Tomcat',
        'udp': 'UDP',
        'ufw': 'UFW',
        'ups': 'UPS',
        'updates': 'Updates',
        'uptime': 'Uptime',
        'user': 'User',
        'yum': 'YUM',
        'wave': 'Wave',
        'webserver': 'Webserver',
    }

    return default_names.get(id, id.replace('_', ' '))


def get_default_check_name(id, command_name):
    default_names = {
        'apt': 'APT',
        'breeze': 'Breeze',
        'clamd': 'Clamd',
        'deny_tls_version': 'Deny TLS version',
        'dhcp': 'DHCP',
        'dig': 'DIG',
        'disk': 'Disk',
        'disk_smb': 'Disk SMB',
        'dnssec_expiry': 'DNSSEC expire',
        'docker_login': 'Docker login',
        'domain_address_ipv4': 'DNS A',
        'domain_address_ipv6': 'DNS AAAA',
        'dummy': 'Dummy',
        'existing_users': 'Existing users',
        'file_age': 'File age',
        'flexlm': 'Flexlm',
        'ftp': 'FTP',
        'group_members': 'Group members',
        'hpjd': 'HP JD',
        'http': 'Http',
        'icmp': 'ICMP',
        'ide_smart': 'SMART',
        'ifstatus': 'Interface status',
        'imap': 'IMAP',
        'ircd': 'IRCD',
        'jabber': 'Jabber',
        'ldap': 'LDAP',
        'ldaps': 'LDAPS',
        'load': 'Load',
        'log': 'Log',
        'mailq': 'Mail queue',
        'mrt_gtraf': 'MRT gtraf',
        'mysql': 'MySQL',
        'mysql_query': 'MySQL query',
        'nntp': 'NNTP',
        'nntps': 'NNTPS',
        'nt': 'NT',
        'ntp_peer': 'NTP peer',
        'ntp_time': 'NTP time',
        'path_exist': 'Path exist',
        'pgsql': 'PostgreSQL',
        'ping': 'Ping',
        'ping4': 'Ping (ipv4)',
        'ping6': 'Ping (ipv6)',
        'pop': 'POP',
        'procs': 'Procs',
        'radius': 'RADIUS',
        'rpc': 'RPC',
        'running_proc_amavisd': 'Amavisd running',
        'running_proc_apache': 'Apache running',
        'running_proc_bind': 'Bind running',
        'running_proc_clamd': 'Clamd running',
        'running_proc_containerd': 'Containerd running',
        'running_proc_cron': 'Cron running',
        'running_proc_docker': 'Docker running',
        'running_proc_dovecot': 'Dovecot running',
        'running_proc_freshclam': 'Freshclam running',
        'running_proc_httpd': 'Httpd running',
        'running_proc_mysql': 'MySQL running',
        'running_proc_nginx': 'NGINX running',
        'running_proc_opendkim': 'Open DKIM running',
        'running_proc_php_fpm': 'PHP FPM running',
        'running_proc_postfix': 'Postfix running',
        'running_proc_postgres': 'PostgreSQL running',
        'running_proc_postgrey': 'Postgrey running',
        'running_proc_rsyslogd': 'Rsyslogd running',
        'running_proc_sshd': 'SSHD running',
        'running_proc_tomcat': 'Apache Tomcat running',
        'sensors': 'Sensors',
        'simap': 'IMAPS',
        'smtp': 'SMTP',
        'snmp': 'SNMP',
        'spop': 'POPS',
        'ssh': 'SSH',
        'sshd_security': 'SSHD security',
        'ssmtp': 'SMTPS',
        'sudoers_group_members': 'Sudoers group members',
        'swap': 'SWAP',
        'tcp': 'TCP',
        'udp': 'UDP',
        'ufw_status': 'UFW Status',
        'ups': 'UPS',
        'uptime': 'Uptime',
        'users': 'Users',
        'wave': 'Wave',
        'web_access_allow_tls1': 'Allow insecure TLS 1.0',
        'web_access_allow_tls1_1': 'Allow insecure TLS 1.1',
        'web_access_allow_tls1_2': 'Allow secure TLS 1.2',
        'web_access_allow_tls1_3': 'Allow secure TLS 1.3',
        'web_access_certificate': 'Certificate check',
        'web_access_default': 'Default web access',
        'web_access_deny_tls1': 'Deny insecure TLS 1.0',
        'web_access_deny_tls1_1': 'Deny insecure TLS 1.1',
        'web_access_deny_tls1_2': 'Deny secure TLS 1.2',
        'web_access_deny_tls1_3': 'Deny secure TLS 1.3',
        'web_access_http_redirect': 'Http to https redirect',
        'web_access_missing_http_redirect': 'No http redirect check for',
        'wheel_group_members': 'Sudoers (wheel) group members',
        'yum': 'YUM',
    }

    for name in default_names:
        if id.startswith(name + '_'):
            return default_names[name]

    return default_names.get(id, default_names.get(command_name, command_name.replace('_', ' ')))
