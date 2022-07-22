# OSINT
## Common Types of Pentests
* External Network Pentest
* Internal Network Pentest
* Web Application Pentest
* Wireless Pentest
* Mobile Pentest
* Physical Pentest
* etc...
* 5 stages of Ethical hacking
	* Reconnaissance -> Scanning & Enumeration -> Gaining Access -> Maintaining Access -> Covering Tracks
	* Recon
		* Active vs Passive
	* Scanning & Enumeration
		* Nmap, Nessus, Nikto, etc.
	* Gaining Access
		* ("Exploitation")
	* Maintaining Access
	* Covering Tracks
		* Anti-virus Evasion
* https://github.com/hmaverickadams/External-Pentest-Checklist
* Security Assessment: Rules of Engagement
* Client Communication - Through Email
* Reconnaissance / OSINT
	* Passive vs Active
* Web / Host
	* Dehashed for data breaches
## Google
* Using quotes "`<search term>`"
* Using conditionals like AND or OR
* Using site:`website.com`
* Wildcard search operator `*`
* Use -www to remove search results that include www or anything else to leave out
* Google dorking (Google Fu)
	* site:tesla.com password filetype:pdf
	* site:tesla.com pass filetype:pdf
	* site:tesla.com pwd filetype:pdf
	* site:tesla.com credentials filetype:pdf
	* site:tesla.com credentials filetype:xlsx
	* site:tesla.com filetype:xlsx
	* site:tesla.com -www -shop
		* subdomains
	* inurl:password
		* searches in the URL for "password"
	* intitle:password
		* searches in title of website for "password"
* Google Advanced Search
	* "`fname lname`" site:`website`.com

## Email OSINT
* Hunter.io: https://hunter.io/
	* Domain Search
* Phonebook.cz: https://phonebook.cz/ 
* Gmail: https://www.google.com/gmail/
	* Gmail plugin Clearbit: https://connect.clearbit.com/
* Email Address Verifier: 
* Email Hippo: https://tools.emailhippo.com/
* Email Checker: https://email-checker.net/

## Breached Passwords
* DEHASHED: https://www.dehashed.com/

---
## Google Image Search
https://images.google.com
## Yandex image search
https://yandex.com/images/
## Exiftool
```
Syntax: exiftool [OPTIONS] FILE
```

## Google Maps Street View
https://www.google.com/maps/d/viewer?mid=1JEkfH9bJtMKrVCMHrKGPP_QmMys&hl=en_US&ll=37.731904282056895%2C-92.97047165000001&z=5
## Social Media
* LinkedIn
	* WeakestLink Dump (GitHub) browser extension
* Twitter
* Reddit
* TikTok
* Instagram

### Wappalyzer
https://www.wappalyzer.com/
### SpyOnWeb
https://spyonweb.com/
### Google Dorking
* msdorkdump tool

---
## More Website OSINT

### BuiltWith
* Chrome and Firefox extension
* https://builtwith.com

### CentralOPS
* https://centralops.net/co/

### DNSLytics
* https://dnslytics.com

### EXIF Viewer
* https://exif-viewer.com  

### GPS Coordinates
* https://gps-coordinates.net

### WeakestLink
* https://github.com/shellfarmer/WeakestLink

### Oh365 User Finder
* https://github.com/dievus/Oh365UserFinder

### SpyOnWeb
* https://spyonweb.com

### VIRUSTOTAL
* https://www.virustotal.com

### Reddit
* https://old.reddit.com
* https://new.reddit.com

### msDNSScan
* https://github.com/dievus/msdnsscan

### msDorkDump
```bash
python3 .\msdorkdump.py -t tesla.com -d
```
* https://github.com/dievus/msdorkdump

### geeMailUserFinder 
* https://github.com/dievus/geeMailUserFinder

### VisualPing
* https://visualping.io

### ViewDNS
* https://viewdns.com

### More Google Dorking
* inurl:tesla.com
* site:tesla.com

### crt.sh
* https://crt.sh

**wildcard**:
```
%.tesla.com
```

### Pentest-Tools.com
* https://pentest-tools.com

### Sublist3r
* https://github.com/aboul3la/Sublist3r

### SHODAN
* https://www.shodan.io
```
city:atlanta
city:atlanta port:3389
city:atlanta rdp
city:atlanta remote desktop
```

Check images and look at what can be found.

### WayBackMachine
* https://archive.org

### Burp Suite
* Make sure to turn proxy on in the browser.
* Response Headers
```
curl -i <domain>
curl -ski <domain>
```

### LinkedIn
* Look people who are software developers/engineers who might have a GitHub account.
* There may be a way to look at credentials, API keys, etc., they have left in their repositories.

### Social Media
* Badges posted on social media.

### opencorporates
* https://opencorporates.com

### Job Postings
* Indeed, Zip Recruiter, Glassdoor, etc.

---

### AntiScan.Me
https://antiscan.me/

---
### Image OSINT
* PimEyes
https://pimeyes.com/en

### Google Maps OSINT
* Geoguessr
https://www.geoguessr.com
https://somerandomstuff1.wordpress.com/2019/02/08/geoguessr-the-top-tips-tricks-and-techniques/

### Facebook OSINT
* trace labs
https://www.tracelabs.org/

* Intelligence X
https://intelx.io/
https://intelx.io/tools?tab=facebook

---
### whois
```bash
whois <DOMAIN>
```

### Sub Domain Tools
crt.sh
shodan.io

### subfinder
```bash
sudo apt install subfinder
```

```bash
subfinder tcm-sec.com
```

### assetfinder
```bash
sudo go install github.com/tomnomnom/assetfinder@latest
```

```bash
assetfinder tesla.com | grep tesla.com | sort -u 
```
