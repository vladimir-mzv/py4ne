from pysnmp.hlapi import *

snmp_var_version = ObjectIdentity('SNMPv2-MIB','sysDescr',0)
snmp_var_version1 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(), CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107","161")), ContextData(), ObjectType(snmp_var_version))


for r in result:
    for s in r[3]:
        print(s)

print(result)



result2 = nextCmd(SnmpEngine(), CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107","161")), ContextData(), ObjectType(snmp_var_version1),lexicographicMode=False)

for r in result2:
    for s in r[3]:
        print(s)

print(result2)
