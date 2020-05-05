## MSSQL Services
**mssql-vulnerability** - Nmap can be leveraged to scan MsSQL for Known vulnerabilities.

**Example Syntax:**

> nmap -vv -sV -Pn -p [PORT] --script=ms-sql-info,ms-sql-config,ms-sql-dump-hashes --script-args=mssql.instance-port=%s,smsql.username-sa,mssql.password-sa [IP]


***


**mssql-default** - Hydra can be utilized to check the MsSQL database for default credentials.

**Example Syntax:**

> hydra -s [PORT] -C ./wordlists/mssql-default-userpass.txt -u -f [IP] mssql


***