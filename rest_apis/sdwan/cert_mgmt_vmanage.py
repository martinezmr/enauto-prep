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

### get list of devices using certificates
cert_endpoint = "/dataservice/certificate/vsmart/list"

headers = {
    "Accept": "application/json"
}
cert_response = sess.get(
    url=f"{base_url}{cert_endpoint}",
    headers=headers,
    verify=False
).json()

print(json.dumps(cert_response, indent=2))

