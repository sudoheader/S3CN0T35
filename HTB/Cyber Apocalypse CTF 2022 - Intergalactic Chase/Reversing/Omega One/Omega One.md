# Omega One
CHALLENGE INFO

You've been sent to the library planet Omega-One. Here, records from all over the galaxy are collected, sorted and archived with perfect efficiency. You need to retrieve records about Draeger's childhood, but the interface is impossibly large. Can you unravel the storage system?

After download the zip, unzipping, we find two files: **ouput.txt** and **omega-one**. 
1. Let's take a look at **output.txt**.
It just a list of words in it:
![[Contents  of output file.png]]
2. 
Now let's look at **omega-one** and try to run it:
![[Running omega-one binary.png]]
There is no output so let's load up `radare2` for our next phase.

```base
r2 -A omega-one
```

3. First do `aaa` which "Analyzes Everything" (skip if using `-A` option), then `afl`, and lastly `pdf @main` :
![[Analyzing with radare2.png]]
Those are some interesting function names.

