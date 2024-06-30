import requests
import json
from pprint import pprint as pp
import urllib3

urllib3.disable_warnings()

router = {
    "host": "192.168.72.136",
    "port": "443",
    "username": "cisco",
    "password": "cisco"
}

# url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-routing:routing"
url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

headers ={
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

response = requests.get(url=url,
                        headers=headers,
                        auth=(router['username'],router['password']),
                              verify=False)

formattedResponse = response.json()

if response.status_code == 200:
    print(json.dumps(formattedResponse, indent=2))
else:
    print(response.status_code)