# Dig Dug Walkthrough
Turns out this machine is a DNS server - it's time to get your shovels out!

Oooh, turns out, this **MACHINE_IP** machine is also a DNS server! If we could `dig` into it, I am sure we could find some interesting records! But... it seems weird, this only responds to a special type of request for a `givemetheflag.com` domain?

  

**Access this challenge** by deploying both the vulnerable machine by pressing the green "Start Machine" button located within this task, and the TryHackMe AttackBox by pressing the  "Start AttackBox" button located at the top-right of the page.

Use some common DNS enumeration tools installed on the AttackBox to get the DNS server on **MACHINE_IP** to respond with the flag.

  

Check out similar content on TryHackMe:

-   [DNS in detail](https://tryhackme.com/room/dnsindetail)
-   [Passive Reconnaissance](https://tryhackme.com/room/passiverecon)
-   [DNS Manipulation](https://tryhackme.com/room/dnsmanipulation)

*Answer the questions below*

Retrieve the flag from the DNS server

---
## Walkthrough
You will need to have `dig` installed on your system. Many Linux distributions like Kali and of course the AttackBox have this installed by default.
Try to first `dig` for the **MACHINE_IP**.
```bash
dig <MACHINE_IP>
```
[First dig output](first_dig_output.png)
![[first_dig_output.png]]
You won't get very far here and its essentially a rabbit hole if you try the other domains. 

If you scan for open port on the machine with `nmap`, you'll find that port 53 is closed. SSH is open on port 22 but we won't focus on that for this task. 
[Nmap Dig Dug](nmap_digdug.png)
![[nmap_digdug.png]]
Instead, let us look at some other DNS reconnaissance tools.

After trying out some commonly used DNS enumeration tools, like `dnsrecon`, `dnsenum`, and `nslookup`, I tried to `dig` one more time. 
If you notice from the room description that the domain `givemetheflag.com` is the only one that this machine will respond to.

Research a bit about using `dig` and how to query a DNS server with a TXT record. 
You will find the command like the one below to work for this room:
```bash
dig -t txt -p53 @<MACHINE_IP> givemetheflag.com
```
[Dig Dug flag output](digdug_output.png):
![[digdug_output.png]]

#tryhackme #dns #domain #name #server #ip #port #nmap #txt #record #dig #tmux #enumeration #kali #recon #reconnaissance #ssh skip this one #flag