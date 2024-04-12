import requests

url = "https://rpc.mywebapi.com/getEmployeeNameById"

data = {"id": "1942-A"}

response = requests.get(url=url,data=data)