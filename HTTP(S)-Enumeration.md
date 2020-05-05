## HTTP/S Services
**Nmap Scripts** - Nmap can be leveraged to scan the service via the Nmap Scanning Engine (NSE). This is helpful when attempting to identify vulnerabilities or potential avenues of attack.

**Example Syntax:**

> nmap -Pn -sV -sC -vvvvv -p[PORT] [IP] -oA [OUTPUT]


***

**Nikto** - Nikto is a web application scanner that looks for thousands of vulnerabilities. This is something you should kick off early and review the results once the scan has completed.

**Example Syntax:**

> nikto -o "[OUTPUT].txt" -p [PORT] -h [IP]

***

**Whatweb** - Whatweb identifies websites and provides insight into the respective web technologies utilized within the target website.

**Example Syntax:**

> whatweb [IP]:[PORT] --color=never --log-brief="[OUTPUT].txt"



***



**CeWL** - CeWL creates customer wordlists based on a specific URL by crawling the web page and picking relevant words. This can be utilized to assist in bruteforcing web page logins.

**Example Syntax:**

If http:

> http://_[IP]_:_[PORT]_/ -m 6, "http,https,ssl,soap,http-proxy,http-alt"

If https:

> https://_[IP]_:_[PORT]_/ -m 6, "http,https,ssl,soap,http-proxy,http-alt"


***


**wafw00f** - Wafw00f identifies if a particular web address is behind a web application firewall.

**Example Syntax:**

If http:

> wafw00f http://_[IP]_:_[PORT]_, "http,https,ssl,soap,http-proxy,http-alt"

If https:

> wafw00f https://_[IP]_:_[PORT]_, "http,https,ssl,soap,http-proxy,http-alt"

***

**w3m** - w3m can be utilized to quickly grab the robots.txt from a website.

**Example Syntax:**

> w3m -dump _[IP]_/robots.txt


***


**Gobuster** - Gobuster is a directory/file busting tool for websites written in Golang. This tool can be run multiple ways, but two main busting strategies are almost always used:
1. Utilize a wordlist of common files/directories.
2. Utilize a wordlist of common cgis.

**Common Directory Busting Example Syntax:**

If http:

> gobuster -w /usr/share/wordlists/SecLists/Discovery/Web_Content/common.txt -u http://[IP]:[PORT] -s "200,204,301,307,403,500"

If https:

> gobuster -w /usr/share/wordlists/SecLists/Discovery/Web_Content/common.txt -u https://[IP]:[PORT] -s "200,204,301,307,403,500"

**Common CGI Busting Example Syntax:**

If http:

> gobuster -w /usr/share/wordlists/SecLists/Discovery/Web_Content/cgis.txt -u http://[IP]:[PORT] -s "200,204,301,307,403,500"

If https:

> gobuster -w /usr/share/wordlists/SecLists/Discovery/Web_Content/cgis.txt -u https://[IP]:[PORT] -s "200,204,301,307,403,500"



***

**Dirbuster** - Dirbuster is a java application designed to brute force web directories/file names. This application can be configured to utilize your preferred wordlist. 

**Example Syntax:**

> gobuster -w /usr/share/wordlists/SecLists/Discovery/Web_Content/common.txt -u http://[IP]:[PORT] -s "200,204,301,307,403,500"

***

**Netcat Banner Grab** - Netcat can be used to grab the service banner of the running application.

**Example Syntax:**

> nc -v -n -w1 [IP] [PORT]


***

**Netcat Banner Grab** - Curl can be used to grab the service banner of the running application.

**Example Syntax:**

> curl -i [IP]


***

**X11 Screenshot** - X11 Screenshot can be used to take a screenshot of the web page.

**Example Syntax:**

> bash ./scripts/x11screenshot.sh [IP]


***


