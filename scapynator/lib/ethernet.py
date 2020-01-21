import scapy

class Ethernet:

    def __init__(self, mac_src, mac_dst):
        self.mac_src = mac_src
        self.mac_dst = mac_dst

    def get_mac_src(self):
        return self.mac_src

    def get_mac_dst(self):
        return self.mac_dst