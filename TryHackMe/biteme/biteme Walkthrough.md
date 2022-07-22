# biteme
##### Description: Stay out of my server!
Difficulty: Medium

###### Task 1:
Start the machine and get the flags...

Answer the questions below

What is the user flag?

What is the root flag?

## Enumeration
First things first, copy the IP address and save it as is:
```bash
export IP=<IP-Address>
```

Now start a `nmap` scan:
```bash
nmap -T4 -p- -A $IP -oA $IP-bitemescan
```
Let it run for a minute. 

## Directory searching