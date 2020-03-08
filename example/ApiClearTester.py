
import requests

url = 'http://127.0.0.1:5000/cmd'

command = {'clear': 'all'} # It clears  used_prixies.txt and clears proxies.txt
#command = {'clear': 'used_proxies'} #  It clears used_prixies.txt
#command = {'clear': 'proxies'}      # It clears proxies.txt

x = requests.post(url, json = command)

print(x.text)