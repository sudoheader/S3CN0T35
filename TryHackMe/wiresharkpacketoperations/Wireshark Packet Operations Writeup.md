# Wireshark: Packet Operations Writeup

### Task 1: Introduction

*Answer the questions below*
1. Read the task above.
```
No answer needed
``` 

### Task 2: Statistics | Summary

*Answer the questions below*
1. Investigate the resolved addresses. What is the IP address of the hostname starts with "bbc"?

Go to "Statistics" and select "Resolved Addresses". In the new window, search for "bbc" and you should get back the IP address.
![[IP of hostname bbc.png]]

Answer:
```
199.232.24.81
```
2. What is the number of the TCP Data packets?

Go to "Statistics" and select "Protocol Hierarchy". In the new window, scroll down to "Transmission Control Protocol" and then take a look at "Data". Look at the "Packet" column, and there should be your answer.
![[Number of TCP data packets.png]]
Answer:
```
1971
```
3. What is the number of IPv4 conversations?

Go to "Statistics" and select "Conversations". In the new window, you'll see the number of packets for each protocol and for IPv4, we have the number already displayed on the second tab.
![[Number of IPv4 conversations.png]]

Answer:
```
435
```
4. How many bytes (k) were transferred from the "Micro-St" MAC address?

Go to "Statistics" and select "Endpoints". In the "Ethernet" tab, make sure you have "Name resolution" checked, and you should be able to see "Micro-St" as part of the set of MAC addresses. The answer will be in the "Bytes" column.
![[Number of transferred bytes from Micro-St.png]]

Answer:
```
7474
```
5. What is the number of IP addresses linked with "Kansas City"?

Go to "Statistics" and select "Endpoints". In the IPv4 tab, scroll to the right and click on City. This should filter by city names from A-Z and if you scroll downward to the K's, you should see "Kansas City". 
![[Number of Kansas City IPs.png]]

Answer:
```
4
```
6. Which IP address is linked with "Blicnet" AS Organisation?

Go to "Statistics" and select "Endpoints". In the IPv4 tab, scroll to the right and click on AS Organization. This should filter by AS Organization names from A-Z and if you scroll downward to the B's, you should see "Blicnet d.o.o". 
![[Blicnet Organization.png]]

Scroll to the right, and you should see the IP address.
![[Blicnet IP address.png]]

Answer:
```
188.246.82.7
```

### Task 3: Statistics | Protocol Details

*Answer the questions below*
1. What is the most used IPv4 destination address?

Go to "Statistics", "IPv4 Statistics" and click on "Destinations and Ports".
![[Path to Destinations and Ports.png]]
A new window should pop up, so wait until the operation has completed. Now click on the "Count" column two times and the IP should be the first one:
![[Most used IPv4 destination address.png]]

Answer:
```
10.100.1.33
```
2. What is the max service request-response time of the DNS packets?

Go to "Statistics" and click on "DNS".
![[Path to DNS Statistics.png]]
A new window should pop up and in "Service Stats" for the Topic/item for "request-reponse time (secs)", the column "Max val" will contain the answer:
![[request-reponse time max value.png]]

Answer:
```
0.467897
```
3. What is the number of HTTP Requests accomplished by "rad[.]msn[.]com?

Answer:
```
39
```

### Task 4: Packet Filtering | Principles

*Answer the questions below*
1. Read the task above.
```
No answer needed
``` 

### Task 5: Packet Filtering | Protocol Filters 

*Answer the questions below*
1. What is the number of IP packets?

Filter:
```
ip
```

Answer:
```
81420
```

2. What is the number of packets with a "TTL value less than 10"?

Filter:
```
ip.ttl < 10
```

Answer:
```
66
```

3. What is the number of packets which uses "TCP port 4444"?

Filter:
```
tcp.port == 4444
```

Answer:
```
632
```

4. What is the number of "HTTP GET" requests sent to port "80"?

Filter:
```
http.request.method == GET && tcp.port == 80
```

Answer:
```
527
```

5. What is the number of "type A DNS Queries"?

Filter:
```
dns.a
```

Answer:
```
51
```


### Task 6: Advanced Filtering

*Answer the questions below*

1. Find all Microsoft IIS servers. What is the number of packets that did not originate from "port 80"?

Filter:
```
http.server contains "Microsoft-IIS" && tcp.srcport != 80
```

Answer:
```
21
```

2. Find all Microsoft IIS servers. What is the number of packets that have "version 7.5"?

Filter:
```
http.server contains "Microsoft-IIS/7.5"
```

This works also:
```
http.server contains "Microsoft-IIS" && http.server matches "7.5"
```

Answer:
```
71
```

3. What is the total number of packets that use ports 3333, 4444 or 9999?

Filter:
```
tcp.port in {3333 4444 9999}
```

Answer:
```
2235
```

4. What is the number of packets with "even TTL numbers"?

The hint says to use the `string()` operator along with a regex to match for even numbers, in this case ending with 0, 2, 4, 6, or 8. 

Filter:
```
string(ip.ttl) matches "[02468]$"
```

Answer:
```
77289
```

5. Change the profile to "Checksum Control". What is the number of "Bad TCP Checksum" packets?

For this one, change the profile by going to "**Edit > Configuration Profiles...**" (Ctrl+Shift+A), select "Checksum Control" in the new window, and press OK. You can also do this by going to the bottom right-hand side of Wireshark and pressing on "Profile: Default", where you can easily switch to "Checksum Control".

Filter:
```
tcp.checksum.status == "Bad"
```

Answer:
```
34185
```
6. Use the existing filtering button to filter the traffic. What is the number of displayed packets?

For this one, make sure you have changed your profile to "Checksum Control", as in the previous question. Once that is done, next to the "Apply a display filter ..." field, there should be a "+" button and next to that another button that says "gif/jpeg with http-200". Press on that button and that should apply the filter that we are looking for. In case there is a problem, you can try out the filter below that does the same thing.

Filter:
```
(http.response.code == 200 ) && (http.content_type matches "image(gif||jpeg)")
```

Answer:
```
261
```