# Enumerating subdomains
* [`amass`](https://github.com/OWASP/Amass)
* [`findomain`](https://github.com/Edu4rdSHL/findomain)
* [`crtsh`](https://github.com/appsecco/the-art-of-subdomain-enumeration/blob/master/crtsh_enum_web.py)
* [`assetfinder`](https://github.com/tomnomnom/assetfinder)
* [`subbrute`](https://github.com/TheRook/subbrute)

`amass` is a tool developed by the OWASP® Foundation and is useful for sub-domain discovery but can be used for much more than that. 
`amass --help` for more info.
Usage:
```bash
amass enum -d docs.google.com
```

`findomain` is "The complete solution for domain recognition"
`findomain --help` for more info.
Usage:
```bash
findomain -t docs.google.com
```

`crtsh_enum_web.py` is a very simple python script using [crt.sh](https://crt.sh/) for searching certificates.
