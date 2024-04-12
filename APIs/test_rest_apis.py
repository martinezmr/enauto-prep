import requests
from pprint import pprint as pp

base_url = "http://httpbin.org/"
## Can allows use the base url above to run APIs

def get_delay(url,seconds):
    endpoint = f"/delay/{seconds}"
    print(f"Getting with {seconds} delay ...")

    resp = requests.get(url+endpoint)
    data = resp.json()
    pp(data)

get_delay(url=base_url,seconds=5)
