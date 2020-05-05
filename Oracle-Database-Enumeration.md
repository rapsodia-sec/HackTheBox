## MsSQL
**oracle-version** - Metasploit can be leveraged to scan the Oracle DB to find the respective version.

**Example Syntax:**

> msfcli auxiliary/scanner/oracle/tnslsnr_version rhosts=[IP] E


***


**oracle-sid** - Metasploit can be utilized to enumerate the Oracle DB SID.

**Example Syntax:**

> msfcli auxiliary/scanner/oracle/sid_enum rhosts=[IP] E


***

**oracle-** - Hydra can be used to check for default Oracle DB credentials.

**Example Syntax:**

> hydra -s [PORT] -C ./wordlists/oracle-default-userpass.txt -u -f [IP]


***