from dnac_functions.get_token import get_token

base_url = "https://sandboxdnac2.cisco.com/dna"
username = "devnetuser"
password = "Cisco123!"

token = get_token(base_url,username,password)
print(token)