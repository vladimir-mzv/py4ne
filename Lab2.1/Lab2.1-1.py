import requests, pprint, json
from textops import *


host_ip = "10.31.70.210"
login = "restapi"
passwd = "j0sg1280-7@"

host_url = 'https://' + host_ip + ':55443'

r = requests.post(host_url + '/api/v1/auth/token-services', auth=(login,passwd), verify = False)
token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}

r = requests.get(host_url + '/api/v1/interfaces', headers = header, verify = False)
#pprint.pprint(r.json())

# GigabitEthernet/Statistics


#pprint.pprint(r.json()['items'][3]['if-name'])

myifs = r.json()['items']
#print(myifs)
for i in myifs:
    ifname = i['if-name']
    print("-----------------------------")
    print(ifname + '  statistics below: ')
    print("-----------------------------")
    pprint.pprint(requests.get(host_url + '/api/v1/interfaces/' + ifname + '/statistics', headers = header, verify = False).json())


