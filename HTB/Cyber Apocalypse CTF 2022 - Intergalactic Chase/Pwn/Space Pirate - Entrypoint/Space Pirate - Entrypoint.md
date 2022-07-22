# Space Pirate: Entrypoint

CHALLENGE INFO

> D12 is one of Golden Fang's missile launcher spaceships. Our mission as space pirates is to highjack D12, get inside the control panel room, and access the missile launcher system. To achieve our goal, we split the mission into three parts. In this part, all we need to do is bypass the scanning system and open the gates so that we proceed further.

First download the **pwn_sp_entrypoint.zip** file, unzip it, and check out the files and folders of the directory **challenge**.
There are a few files in **glibc** we can look at later but besides that the **flag.txt** is just a test file and **sp_entrypoint** is an ELF 64-bit LSB pie executable.
* File info:
```bash
file sp_entrypoint
```
- Running the file:
```base
./sp_entrypoint
```
![[Running executable.png]]
If you try **1**, it'll say something is wrong and that you need to insert the card's serial number, which we don't have.
If you try **2**, it'll say to Insert password:
![[Selecting to Insert Password.png]]

At this point, you can try out any password and get a fake flag as the passphrase, but you'll get a flashing "**Intruder detected!**" in the terminal. Notice that the menu color alternates:
![[Fake flag.png]]

There is a way to output what looks like the password from the program by doing:
```bash
strings sp_entrypoint | grep -A 1 password
```
![[Grepping for password did not work.png]]

However this is not the password for the program so it won't work--it only accepts 16 characters for the password.
