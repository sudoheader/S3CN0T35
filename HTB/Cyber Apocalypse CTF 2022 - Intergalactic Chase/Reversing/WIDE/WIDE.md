# WIDE
CHALLENGE INFO

WIDE

We've received reports that Draeger has stashed a huge arsenal in the pocket dimension Flaggle Alpha. You've managed to smuggle a discarded access terminal to the Widely Inflated Dimension Editor from his headquarters, but the entry for the dimension has been encrypted. Can you make it inside and take control?

## Walkthrough
1. Download `rev_wide.zip` and unzip it.
2. In it, you'll find two files `db.ex` and a binary file`wide`. Try `file db.ex` and `file wide` to see more info.
```bash
file db.ex
```
![[Determining what db.ex is.png]]
```bash
file wide
```
![[Determinig what wide is.png]]
3. Try running the program:
```base
./wide
```
![[Runing wide needs db.ex.png]]
You'll see that the usage should be with the database file so supply it with that:
```base
./wide db.ex
```
![[Running wide with db.ex.png]]

If you try with anything from Name, Code, or just jibberish, the program will keep outputting **Our home dimension**.
Try with numbers instead, like 0, 1, 2, etc...

![[Selecting 6 as the dimension.png]]

You should notice that  "Flaggle Alpha" is the 7th name in the list--it starts from 0--so subtract 1 to get to 6. Try 6 now:
![[WIDE decryption key prompt.png]]
If you try any combination in the list, you won't get very far so skip trying to brute force it. 

We will use `radare2`

4. Now install `radare2` if you don't have it already and launch it with:
```bash
r2 -A wide
```
5. First do `aaa` which "Analyzes Everything" (skip if using `-A` option), then `afl`, and lastly `pdf @main` :
![[Running wide in radare2.png]]
You should notice something important about the functions in the program. **sym.menu** is the function for our menu.

Let's take a look at **sym.menu**:
![[Menu functions for wide.png]]

Scrolling down, you'll see many variables set for the function and other assembly code.
Keep going until after you reach the **That entry is encrypted** text.

You should see the password listed after `str.` and after the semi colon.

Hmm I wonder what this could be?

![[Hmm.png]]

Now that we have our password, we should use this to solve the challenge:
```bash
./wide db.ex
```

Enter **6** for the dimension to examine and then the password. You'll should now get the flag.

![[Flag.png]]