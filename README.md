# **Home Lab: Building a Basic Port Scanner with Python**

**Project:** TCP Port Scanner

**Author:** César Asto Oré

**Start date:** 06/09/2026

**End date:** In progress

## Overview

## Architecture

## Toolbox
- Kali Linux: attacker machine
- Ubuntu Desktop: target machine
- Visual Studio Code: code editor
- Python: scripting language

## Implementation


### Attacker Machine

```plaintext
┌──(kali㉿kali)-[~]
└─$ ping -c 4 10.0.0.102

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 21
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 21 (ftp) open

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 22
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 22 (ssh) open

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 80
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 80 (http) open

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 53 
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 53 (domain) : Connection refused

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 631
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 631 (ipp) : Connection refused

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 8080
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 8080 (http-alt) : Connection refused

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 9999
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 9999 (?) : Connection refused

```

After adding rules in firewall:

```plaintext
┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 21
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 21 (ftp) open

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 8080
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 8080 (http-alt) : Connection refused

┌──(kali㉿kali)-[~]
└─$ nc -zv 10.0.0.102 9999
10.0.0.102: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [10.0.0.102] 9999 (?) : Connection timed out
```

### Target Machine

```plaintext
ubuntu@StevensUbuntu:~$ ping -c 4 10.0.0.101
ubuntu@StevensUbuntu:~$ sudo ss -tlnp

ubuntu@StevensUbuntu:~$ sudo apt install openssh-server
ubuntu@StevensUbuntu:~$ sudo apt install ssh-apache2
ubuntu@StevensUbuntu:~$ sudo apt install ssh-vsftpd

ubuntu@StevensUbuntu:~$ systemctl status ssh
○ ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; disabled; preset: ena...
     Active: inactive (dead)
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)

ubuntu@StevensUbuntu:~$ systemctl status apache2
● apache2.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/apache2.service; enabled; preset: ...)
     Active: active (running) since Sun 2026-09-06 16:42:53 -05; 24min ago
   Invocation: 7344b28e5f914881831e85b61474a f6b
       Docs: https://httpd.apache.org/docs/2.4/
   Main PID: 6046 (apache2)
     Status: "Total requests: 0; Idle/Busy workers 100/0;Requests/sec: 0; Bytes...>
      Tasks: 55 (limit: 8365)
     Memory: 5.9M (peak: 6.1M)
        CPU: 97ms
     CGroup: /system.slice/apache2.service
             ├─6046 /usr/sbin/apache2 -k start -DFOREGROUND
             ├─6062 /usr/sbin/apache2 -k start -DFOREGROUND
             └─6063 /usr/sbin/apache2 -k start -DFOREGROUND

Sep 06 16:42:53 StevensUbuntu systemd[1]: Starting apache2.service - The Apache...
Sep 06 16:42:53 StevensUbuntu apachectl[6046]: AH00558: apache2: Could not reli...
Sep 06 16:42:53 StevensUbuntu systemd[1]: Started apache2.service - The Apache ...

ubuntu@StevensUbuntu:~$ systemctl status vsftpd
● vsftpd.service - vsftpd FTP server
     Loaded: loaded (/usr/lib/systemd/system/vsftpd.service; enabled; preset: e...)
     Active: active (running) since Sun 2026-09-06 16:43:05 -05; 24min ago
   Invocation: e9b806e7edf54f9c8a3823f8ade6f5de
   Main PID: 6869 (vsftpd)
      Tasks: 1 (limit: 6365)
     Memory: 916K (peak: 2M)
        CPU: 8ms
     CGroup: /system.slice/vsftpd.service
             └─6869 /usr/sbin/vsftpd /etc/vsftpd.conf

Sep 06 16:43:05 StevensUbuntu systemd[1]: Starting vsftpd.service - vsftpd FTP...
Sep 06 16:43:05 StevensUbuntu systemd[1]: Started vsftpd.service - vsftpd FTP s...

ubuntu@StevensUbuntu:~$ sudo ss -tlnp
State   Recv-Q   Send-Q   Local Address:Port      Peer Address:Port   Process
LISTEN  0        4096     127.0.0.54:53           0.0.0.0:*           users:(("systemd-resolve",pid=415,fd=19))
LISTEN  0        4096     127.0.0.1:631           0.0.0.0:*           users:(("cupsd",pid=1261,fd=7))
LISTEN  0        4096     127.0.0.53%lo:53        0.0.0.0:*           users:(("systemd-resolve",pid=415,fd=17))
LISTEN  0        4096     0.0.0.0:22              0.0.0.0:*           users:(("sshd",pid=9046,fd=3),("systemd",pid=1,fd=156))
LISTEN  0        4096     [::1]:631               [::]:*              users:(("cupsd",pid=1261,fd=6))
LISTEN  0        511      *:80                    *:*                 users:(("apache2",pid=6063,fd=4),("apache2",pid=6062,fd=4),("apache2",pid=6046,fd=4))
LISTEN  0        4096     [::]:22                 [::]:*              users:(("sshd",pid=9046,fd=4),("systemd",pid=1,fd=157))
LISTEN  0        32       *:21                    *:*                 users:(("vsftpd",pid=6869,fd=3))

ubuntu@StevensUbuntu:~$ sudo ufw allow 21/tcp
ubuntu@StevensUbuntu:~$ sudo ufw allow 22/tcp
ubuntu@StevensUbuntu:~$ sudo ufw allow 80/tcp
ubuntu@StevensUbuntu:~$ sudo ufw reject 8080/tcp
ubuntu@StevensUbuntu:~$ sudo ufw enable

ubuntu@StevensUbuntu:~$ sudo ufw status
Status: active

To              Action      From
--              ------      ----
22/tcp          ALLOW       Anywhere
21/tcp          ALLOW       Anywhere
80/tcp          ALLOW       Anywhere
8080/tcp        REJECT      Anywhere
22/tcp (v6)     ALLOW       Anywhere (v6)
21/tcp (v6)     ALLOW       Anywhere (v6)
80/tcp (v6)     ALLOW       Anywhere (v6)
8080/tcp (v6)   REJECT      Anywhere (v6)

```

## Results

## Lessons learned

## Next steps
