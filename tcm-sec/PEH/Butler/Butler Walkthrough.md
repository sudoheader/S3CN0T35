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
![[Pasted image 20220304122804.png]]

Trying to connect to `telnet <IP-Address> 7680` will be "Trying" but to no avail. `netcat` will also result in the same issue. Also going to the browser on http://IP-Address:7680 will not work either because it is not a web address. We get to a Jenkins login screen on port 8080 and if we search online for default login credentials for Jenkins, we get `admin:password` as one of them. However, trying this out results in "Invalid username or password".
![[Pasted image 20220304124046.png]]

So open up Burp Suite and set Foxy Proxy to intercept the request.
After submitting, you should get:
![[Pasted image 20220304151412.png]]

Right click and "Send to Repeater" and also do it for "Send to Intruder" (Ctrl-R, Ctrl-I for short). In Repeater, if we press the "Send" button, we get a "302 Found" and then if you press on the "Follow redirection" button, we get "401 Unauthorized".
![[Pasted image 20220304152444.png]]

We can brute force this with Repeater, but it is inefficient so jump to the Intruder tab.

Now go into the Positions tab and hit the "Clear §" button. The "§" should all be gone now in this POST request. Double click on the field where it says "admin" and hit the "Add §" button. Do the same for the password value. It should look like this:
![[Pasted image 20220304152859.png]]

Make sure that the "Attack type" is set to "Cluster bomb":
![[Pasted image 20220304153030.png]]

Go to the "Payloads" tab and for the first Payload set (1) add these values for the username field: admin, administrator, jenkins:
![[Pasted image 20220304153404.png]]

In the second payload set (2) add these values: password, jenkins, Password, Jenkins, Password1
![[Pasted image 20220304153623.png]]

Now, you can start attack by pressing on the "Start attack" button:
![[Pasted image 20220304154630.png]]

Go to the Proxy tab and make sure "Intercept is off". The credentials `jenkins:jenkins` should log us in.
