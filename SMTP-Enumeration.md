## SMTP Services
**smtp-enum-vrfy** - Metasploit can utilize the VRFY verb to enumerate SMTP servers.

**Example Syntax:**

> smtp-user-enum -M VRFY -U /usr/share/metasploit-framework/data/wordlists/unix_users.txt -t [IP] -p [PORT]

***

**smtp-enum-expn** - Metasploit can utilize the EXPN verb to enumerate SMTP servers.

**Example Syntax:**

> smtp-user-enum -M EXPN -U /usr/share/metasploit-framework/data/wordlists/unix_users.txt -t [IP] -p [PORT]


***

**smtp-enum-rcpt** - Metasploit can utilize the RCPT verb to enumerate SMTP servers.

**Example Syntax:**

> smtp-user-enum -M RCPT -U /usr/share/metasploit-framework/data/wordlists/unix_users.txt -t [IP] -p [PORT]


***