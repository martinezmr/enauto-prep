from ncclient import manager
import logging
from pprint import pprint as pp
import xmltodict

## this will debug the script each step
# logging.basicConfig(level = logging.DEBUG)

router = {
    "host": "192.168.72.136",
    "port": "830",
    "username": "cisco",
    "password": "cisco"
}

## using ** will unpack the values in the parentheses
# like this manager.connect("host"="", "port": "830", etc etc)
# with manager.connect(**router, hostkey_verify=False) as m:
#     for capability in m.server_capabilities:
#         print("#" * 25)
#         print(" ")
#         print(capability)

interface_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces-state>
</filter>
"""

with manager.connect(**router, hostkey_verify=False) as m:
    netconf_response = m.get(interface_filter)

python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
pp(python_response)