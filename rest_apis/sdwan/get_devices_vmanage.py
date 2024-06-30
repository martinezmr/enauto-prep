import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandbox-sdwan-2.cisco.com"
auth_endpoint = "/j_security_check"

auth = {
    "j_username": "devnetuser",
    "j_password": "RG!_Yw919_83"
}

### auth with vmanage
sess = requests.session()
login_response = sess.post(
    url=f"{base_url}{auth_endpoint}",
    data=auth,
    verify=False
)

### get device list
device_endpoint = "/dataservice/device"
device_response = sess.get(
    url=f"{base_url}{device_endpoint}",
    verify=False
).json()

print(json.dumps(device_response, indent=2))

