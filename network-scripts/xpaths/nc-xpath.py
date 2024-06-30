from scrapli_netconf.driver import NetconfScrape

my_device = {
    "host": "10.10.21.15",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfScrape(**my_device)
conn.open()

## do not have to call out the xml namespace making it easier than netconf calls
ospf_xpath = '/ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id="1683409"]'
response = conn.get(
    filter_= ospf_xpath, filter_type='x'
)
print(response.result)