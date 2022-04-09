# Networking
`ifconfig`
	
inet 192.168.XX.XX  
8 bits . 8 bits . 8 bits . 8 bits  
0.0.0.0 -> 255.255.255.255  
private ip address  
  
layer 3 protocol  
  
---  
  
ether 00:0c:29  
hexadecimal  
  
MAC addresses -> Layer 2 related to switching  
  
---  
  
## TCP vs UDP  
### Transport Layer Protocol / User Datagram Protocol
TCP: connection oriented. Reliable  
HTTP/S, SSH, FTP  
  
UDP: connection-less. Unreliable  
DNS, VOIP  
  
Scanning both  
Most common: TCP  
  
SYN > SYN ACK > ACK  
  
HTTP: 80  
HTTPS: 443  
  
Common Ports and Protocols  
TCP: UDP:  
FTP (21) DNS (53)  
SSH (22) DHCP (67, 68)  
Telnet (23) TFTP (69)  
SMTP (25) SNMP (161)  
DNS (53)  
HTTP (80) / HTTPS (443)  
POP3 (110)  
SMB (139 + 445)  
IMAP (143)  
  
---  
## OSI Model  
  
**Mnemonic: Please Do Not Throw Sausage Pizza Away** 
  
1 Physical - data cables, cat6  
2 Data Link- Switching, MAC addresses  
3 Network - IP addresses, routing  
4 Transport - TCP/UDP  
5 Session - session management  
6 Presentation - WMV, JPEG, MOV  
7 Application - HTTP, SMTP  

  | #   | Layer        | Usage                    |
  | --- | ------------ | ------------------------ |
  | 1   | Physical     | data cables              |
  | 2   | Data Link    | Switching, MAC addresses |
  | 3   | Network      | IP addresses, routing    |
  | 4   | Transport    | TCP/UDP                  |
  | 5   | Session      | session managment        |
  | 6   | Presentation | WMV, JPEG, MOV           |
  | 7   | Application  | HTTP, SMTP               |

---  
  
## Sub-netting
  
255.255.255.0 => /24 network $2^8 = 256$ hosts available

	|                 | Subnet          | Hosts | Network      | Broadcast     |
	| --------------- | --------------- | ----- | ------------ | ------------- |
	| 192.168.1.0/24  | 255.255.255.240 | 254   | 192.168.1.0  | 192.168.1.255 |
	| 192.168.1.0/28  | 255.255.255.240 | 14    | 192.168.1.0  | 192.168.1.15  |
	| 192.168.1.16/28 | 255.255.255.240 | 14    | 192.168.1.16 | 192.168.1.31  |
	| 192.168.0.0/23  | 255.255.254.0   | 510   | 192.168.0.0  | 192.168.1.255 |
	| 192.168.2.0/23  | 255.255.254.0   | 510   | 192.168.2.0  | 192.168.3.255 |
	|                 |                 |       |              |               |
	| 192.168.0.0/22  | 255.255.252.0   | 1022  | 192.168.0.0  | 192.168.3.255 |
	| 192.168.1.0/26  | 255.255.255.192 | 62    | 192.168.1.0  | 192.168.1.63  |
	| 192.168.1.0/27  | 255.255.255.224 | 30    | 192.168.1.0  | 192.168.1.31  | 

