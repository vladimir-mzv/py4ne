import random
from ipaddress import IPv4Network

class IPv4RandomNetwork(IPv4Network):
    def __init__(self ):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), strict=False)
    def regular(self):
        return self.is_global and not self.is_loopback and not self.is_multicast and not self.is_reserved

    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)

networks = []

for i in range(50):
    rand_net = IPv4RandomNetwork()
    if rand_net.regular() and not rand_net in networks:
        networks.append(str(rand_net))

print(networks)

#def sortedf(x):
#    return x.key_value()

#for n in sorted(networks, key=sortedf):
#    print(n)