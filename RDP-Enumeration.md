## RDP Services
**rdp-sec-check** - RDP security settings can be enumerated via rdp-sec-check.

**Example Syntax:**

> perl ./scripts/rdp-sec-check.pl [IP]:[PORT],


***

## RDP Services
**ncrack** - Ncrack can be utilized to brute force RDP services.
**Example Syntax:**

> ncrack -vv --user administrator -P /usr/share/wordlists/rockyou.txt rdp://[IP]


***