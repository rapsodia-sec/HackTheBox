## FTP Services
**ftp-vulnerability-scan** - Nmap can be leveraged to scan FTP services for known vulnerabilities.

**Example Syntax:**

> nmap -sV -Pn -vv -p [PORT] --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 [IP]


***

**ftp-default** - Hydra can be utilized to check FTP services for default credentials.

**Example Syntax:**

> hydra -s [PORT] -C ./wordlists/ftp-default-userpass.txt -u -f [IP] ftp


***