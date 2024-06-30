import requests
import json

token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = "https://api.meraki.com/api/v1"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Cisco-Meraki-API-Key": token
}

### Get Organizations
endpoint = "/organizations"
try:
    response = requests.get(
        url=f"{base_url}{endpoint}",
        headers=headers,
        verify=False
    ).json()
    print(json.dumps(response,indent=2))
except Exception as e:
    print(e)

