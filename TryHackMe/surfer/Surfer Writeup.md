![[Surfer - room image.png]]
# Surfer Writeup

## Surf some internal webpages to find the flag!

### Task 1 - Surfer
Woah, check out this radical app! Isn't it narly dude? We've been surfing through some webpages and we want to get you on board too! They said this application has some functionality that is only available for internal usage -- but if you catch the right wave, you can probably find the sweet stuff!


Access this challenge by deploying both the vulnerable machine by pressing the green "Start Machine" button located within this task, and the TryHackMe AttackBox by pressing the  "Start AttackBox" button located at the top-right of the page.

Navigate to the following URL using the AttackBox: HTTP://MACHINE_IP


Check out similar content on TryHackMe:

* [SSRF](https://tryhackme.com/room/ssrfqi)

*Answer the questions below*
Uncover the flag on the hidden application page.

#### Walkthrough

After connecting to TryHackMe via VPN or using the **Start AttackBox** button, click on the **Start Machine** button.

##### Recon:
Run an `nmap` scan to check using default scripts, OS detection, and service version detection. 
```bash
nmap -A MACHINE_IP
```

`nmap` terminal output:
```bash
┌──(kali㉿kali)-[~/thm/surfer]
└─$ nmap -A 10.10.87.183 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-14 14:38 EDT
Nmap scan report for 10.10.87.183
Host is up (0.20s latency).
Not shown: 839 closed tcp ports (conn-refused), 159 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 37:e0:e9:4a:07:14:48:fb:fc:9c:12:e9:78:1e:4d:06 (RSA)
|   256 20:7e:cc:44:2f:e7:40:98:86:75:3c:e2:90:85:ce:f8 (ECDSA)
|_  256 c5:c5:61:2b:b7:21:6e:6f:5d:61:69:f2:76:41:dd:05 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
| http-robots.txt: 1 disallowed entry 
|_/backup/chat.txt
| http-title: 24X7 System+
|_Requested resource was /login.php
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.38 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.02 seconds

```

It should reveal to us that the service running on port 80 is Apache httpd, which is open, and one disallowed entry in the **robots.txt** file. We also have an oddity at **/backup/chat.txt**:
![[Surfer - nmap output.png]]

Let's first look at the **robots.txt** file. Browse to the file by going to `MACHINE_IP/backup/robots.txt` in your browser and see what has been disallowed:
![[Surfer - robots.txt.png]]
We can see that the file at **/backup/chat.txt** has been disallowed.

Now take a look at **chat.txt** file. Browse to the file by going to `MACHINE_IP/backup/chat.txt` in your browser and read the conversation:
![[Surfer - chat.txt conversation.png]]
It looks like there is a tool called `export2pdf` installed by the Admin  and that Kate tried to get the admin to update their credentials but didn't reply, suggesting that the admin is probably using their username as a password.

Using **gobuster**, we will try the process of directory brute forcing to find subdirectories used by the web application.
```bash
gobuster dir -u http://MACHINE_IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

`gobuster` terminal output:
```bash
┌──(kali㉿kali)-[~/thm/surfer]
└─$ gobuster dir -u http://10.10.87.183 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt                                              139 ⨯
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.87.183
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/10/14 14:39:09 Starting gobuster in directory enumeration mode
===============================================================
/assets               (Status: 301) [Size: 313] [--> http://10.10.87.183/assets/]
/vendor               (Status: 301) [Size: 313] [--> http://10.10.87.183/vendor/]
/backup               (Status: 301) [Size: 313] [--> http://10.10.87.183/backup/]
/internal             (Status: 301) [Size: 315] [--> http://10.10.87.183/internal/]
/server-status        (Status: 403) [Size: 277]                                    
Progress: 124305 / 220561 (56.36%)                                                ^C
[!] Keyboard interrupt detected, terminating.
                                                                                   
===============================================================
2022/10/14 15:22:26 Finished
===============================================================
```

Notice the directories **backup** and **internal**:
![[Surfer - gobuster.png]]

Now let's try to browse to the **internal** directory in our browser:
![[Surfer - internal 403.png]]
We got a 403 Forbidden HTTP status page.

Since we can't see anything on this page, even when we have already logged in, let's go to the login page.

In your browser, go the the `MACHINE_IP` url and it should redirect to the login page.
![[Surfer - login page.png]]
We need a username and password to access. Hmm, I wonder what we could use that we have just uncovered? 🤔

Do the credentials `admin:admin` work? Yes, indeed it does!

We have arrived at the admin page and are logged in as Admin. You should see the page as shown below:
![[Surfer - admin page.png]]
NOTE: You can check out the admin's profile by clicking on the drop down in the top right corner but there is nothing that's useful to us, except for some funny misspellings 😄.

Scroll down until you see the **Export to PDF** button:
![[Surfer - Export to PDF.png]]

Go back to the Dashboard page and notice something on the right hand where there is a list of **Recent Activity**:
![[Surfer - Recent Activity panel.png]]

It seems the flag is located in **/internal/admin.php**, but remember that we don't have access to the **internal** directory, even after logging in.

To perform the **SSRF**, you'll need **Burp Suite** running in the background. We also need to have the browser set up so **Burp Suite** can intercept requests. Even better, using my preferred method, install a Firefox extension called **FoxyProxy** and have it set up so it has requests intercepted by **Burp Suite** when we click on the **Export to PDF** button.

First, let's take a look at what happens when we click on the button without any intercepts. Making sure that **Intercept is off** in **Burp Suite** and/or **FoxyProxy** is set to **Turn Off (Use Firefox Settings)**, click on the **Export to PDF** button.

NOTE:  this generates the same page, in PDF format, that we get from the Dashboard page, however the Server IP is the localhost IP instead:
![[Surfer - export2pdf.php.png]]

Now let's try intercepting the request and changing it so that we can see what the **/internal/admin.php** is hiding.

Making sure that **Intercept is on** in **Burp Suite** and **FoxyProxy** is set for **Burp Suite** to intercept the request, click on the **Export to PDF** button.

**Burp Suite** should intercept the request, and all we really need to change here is the `server-info.php` text to `internal/admin.php` instead:
![[Surfer - Burp Suite intercepted request on export2pdf.php.png]]

Change it like so:
![[Surfer - SSRF on admin.php.png]]

Click on **Forward** in **Burp Suite** to forward the request.

The browser should load the **export2pdf.php** report in the background. We can now see our flag:
![[Surfer - flag.png]]

We have successfully solved this room!

**FLAG:**
```
flag{6255c55660e292cf0116c053c9937810}
```
