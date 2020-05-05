## MySQL
**mysql-vulnerability** - Nmap can be leveraged to scan MySQL for Known vulnerabilities.

**Example Syntax:**

> nmap -sV -Pn -vv -script=mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122 [IP] -p [PORT]


***


**mysql-default** - Hydra can be utilized to check the MySQL database for default credentials.

**Example Syntax:**

> hydra -s [PORT] -C ./wordlists/mysql-default-userpass.txt -u -f [IP] mysql


***