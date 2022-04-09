# Enumeration
port 80/443 - 172.16.172.131 - 2:42pm
Default webpage - Apache - PHP
Information Disclosure - 404 page
Information Disclosure - server headers disclose version information

80/tcp    open  http        Apache httpd 1.3.20 ((Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b)

mod_ssl/2.8.4 - mod_ssl 2.8.7 and lower are vulnerable to a remote buffer overflow which may allow a remote shell. http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0082, OSVDB-756.

SMB
Unix (Samba 2.2.1a)

Webalizer Version 2.01 - http://172.16.172.131/usage/usage_200909.html

SSH
OpenSSH 2.9p2