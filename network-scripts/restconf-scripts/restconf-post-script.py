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

base_url = f"https://{router['host']}:{router['port']}/restconf/data/"
apiEndpoint = "ietf-interfaces:interfaces/"
url = f"{base_url}{apiEndpoint}"

headers ={
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback100",
        "description": "Updated via Restconf API",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.100.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

response = requests.post(url=url,
                        headers=headers,
                        auth=(router['username'],router['password']),
                        data=json.dumps(payload),
                              verify=False)

# formattedResponse = response.json()

if response.status_code == 200:
    print(response.text)
else:
    print(response.text)