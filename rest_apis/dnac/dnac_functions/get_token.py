import requests
import json

def get_token(url,user,pw):
    auth_endpoint = "/system/api/v1/auth/token"
    auth_response = requests.post(
        url=f"{url}{auth_endpoint}",
        auth=(user,pw),
        verify=False
    ).json()
    token = auth_response["Token"]

    return token

# headers={
#     "x-auth-token": token,
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }

# sites_endpoint = "/intent/api/v1/site"

# site_response = requests.get(
#     url=f"{base_url}{sites_endpoint}",
#     headers=headers,
#     verify=False
# ).json()["response"]

# print(json.dumps(site_response,indent=2))