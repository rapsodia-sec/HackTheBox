## SMB Services
**samrdump** - samrdump communicates with the Security Account Manager Remote interface from the MSRPC suite. It lists system user accounts, available resource shares and other sensitive information exported through this service.

**Example Syntax:**

> python /usr/share/doc/python-impacket-doc/examples/samrdump.py [IP] [PORT]/SMB


***

**smbenum** - smbenum can be utilized to enumerate smb shares.

**Example Syntax:**

> bash ./scripts/smbenum.sh [IP]


***

**smbenum** - smbenum can be utilized to enumerate smb shares.

**Example Syntax:**

> bash ./scripts/smbenum.sh [IP]


***

**enum4linux** - SMB shares can be enumerated via enum4linux.

**Example Syntax:**

> enum4linux [IP]

***

**enum4linux** - SMB shares can be enumerated via enum4linux.

**Example Syntax:**

> enum4linux [IP]


***

**smb-enum-users-rpc** - Users can be enumerated through SMB services via RPCClient.

**Example Syntax:**

> bash -c \"echo 'enumdomusers' | rpcclient [IP] -U%\"


***

**smb-enum-admins** - Net can be utilized to enumerate Domain Administrators via SMB shares.

**Example Syntax:**

> net rpc group members \"Domain Admins\" -I [IP] -U%


***

**smb-enum-groups** - Nmap can be utilized to enumerate groups via SMB.

**Example Syntax:**

> nmap -p[PORT] --script=smb-enum-groups [IP] -vvvvv


***

**smb-enum-shares** - Nmap can be utilized to enumerate shares via SMB.

**Example Syntax:**

> nmap -p[PORT] --script=smb-enum-shares [IP] -vvvvv

***

**smb-enum-sessions** - Nmap can be utilized to enumerate logged in users via SMB.

**Example Syntax:**

> nmap -p[PORT] --script=smb-enum-sessions [IP] -vvvvv

***

**smb-enum-policies** - Nmap can be utilized to password policies via SMB.

**Example Syntax:**

> nmap -p[PORT] --script=smb-enum-domains [IP] -vvvvv

***

**smb-null-sessions** - Rpcclient can be utilized to check for null sessions.

**Example Syntax:**

> bash -c \"echo 'srvinfo' | rpcclient [IP] -U%\"

***

**smb-vulnerability** - Nmap can be utilized to check SMB services for known vulnerabilities.

**Example Syntax:**

> nmap -sV -Pn -vv -p [PORT] --script=smb-vuln* --script-args=unsafe=1 [IP]

***

**nbtscan** - Nbtscan finds the IP address, NetBIOS computer name, logged-in user name and MAC address via SMB.

**Example Syntax:**

> nbtscan -v -h [IP]

***

**Manual Browsing** - SMB Shares should be enumerated manually whenever possible.

**Example Syntax:**

> smbclient -L INSERTIPADDRESS

> smbclient //INSERTIPADDRESS/tmp

> smbclient \\\\INSERTIPADDRESS\\ipc$ -U john

> smbclient //INSERTIPADDRESS/ipc$ -U john

> smbclient //INSERTIPADDRESS/admin$ -U john

> winexe -U username //INSERTIPADDRESS "cmd.exe" --system

***