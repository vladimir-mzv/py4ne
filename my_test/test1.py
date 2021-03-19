class Subnet:
    def __init__(self, n="0.0.0.0" ,p="/0"):
            self.network = n
            self.prefix = p
    def __str__(self):
            return "Network" + self.network + ", prefix " + self.prefix
    def getnet(self):
            return self.network
    def getprefix(self):
            return self.prefix

n1=Subnet("192.168.0.1", "/24")
n2=Subnet("192.168.1.1", "/24")
n3=Subnet("192.168.2.1", "/24")

print(n1.network)