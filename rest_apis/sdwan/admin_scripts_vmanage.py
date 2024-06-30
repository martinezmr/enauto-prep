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

admin_endpoint = "/dataservice/admin/user"

payload = {
    "group": ["netadmin"],
    "description": "Test Data",
    "userName": "admin",
    "password": "C1sco123"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = sess.post(
    url=f"{base_url}{admin_endpoint}",
    headers=headers,
    data=json.dumps(payload),
    verify=False
)

print(response.text)