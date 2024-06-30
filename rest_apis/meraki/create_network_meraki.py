import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = "https://api.meraki.com/api/v1"
org_id = "575334852396585373"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Cisco-Meraki-API-Key": token
}

### Create Network in Organization
endpoint = f"/organizations/{org_id}/networks"
payload = {
    "name": "Phat Cheeks",
    "productTypes": [
        "appliance",
        "switch",
        "wireless"
    ],
    "timeZone": "America/Los_Angeles",
    "notes": "Clapping cheeks"
}
try:
    response = requests.post(
        url=f"{base_url}{endpoint}",
        headers=headers,
        verify=False,
        data=json.dumps(payload)
    ).json()
    print(json.dumps(response,indent=2))
except Exception as e:
    print(e)

