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

url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

headers ={
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

response = requests.get(url=url,headers=headers,auth=(router['username'],router['password']),verify=False)

if response.status_code == 200:
    response_dict = response.json()
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(capability)
else:
    print(response.status_code)