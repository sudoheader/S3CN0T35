## Task 7

This task took me more time than I'd like to admit. Just goes to show what really needs to be practiced over and over.

For this one, if you read the hint, it really does show what you have to do to get the flag (think clearly on this before spoiling it for yourself). Again it says to use the command `ncat -lvnp 443 -c "ncat TARGET_SERVER 25`. However, we will need to replace the destination port, the `TARGET_SERVER`, which says to replace it with the localhost address (127.0.0.1) and also the target server address, in this case replace 25 as well. 

Remember that the description says that, "The firewall is blocking traffic to port 80" and that "port 8008 is not blocked". Taking this to account, we should end up with the command below:
```bash
ncat -lvnp 8008 -c "ncat 127.0.0.1 80"
```
Now go to the browser where we are running the machine from http://<IP-Address>:8080 and enter that command into the field where it says "What is your command?". Click on "Submit Form" once done.

In another tab, go to that http://<IP-Address>:8008 and you should see the flag.