# Kali Linux

`sudo su -`

To switch to root user

`updatedb`
To update database for `locate` . For example to look for `bash` we can do `locate bash` to find references that use the word "bash".

`chmod` : "change mode"

---
## Network commands

`ipconfig`: On Windows, displays all current TCP/IP network configuration values.
`ifconfig`: On Linux, configure a network interface.
`iwconfig`: On laptop, shows "wlan". Otherwise, "no wireless extensions".

`arp -a`: IP address it talks to and the MAC address associated with it. Associating IP addresses with MAC addresses.

`netstat -ano`: Active connections running on machine.
`route`: Prints routing table.

---
### ip
`ip a`: new and improved `ifconfig` alternative with color.
`ip n`: "n" stands for neighbor, similar to `arp` table.
`ip r`: routing table

