"""
Utilisation de scapy pour savoir si des requêtes sur le port spécifié arrive,

fonction rapide d'envoi :
envoi d'une requête HTTP
envoi d'une requête DICOM
envoi d'une requête
"""

from scapy.all import *

class Paquet:

    def __init__(self):
        pass

    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)
        print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

    def capture(self, port, IP_l, IP_r=None):
        print("Capture en cours...")
        if IP_r is not None:
            sniff(filter="dst port " + port + " and src host " + IP_r + " and dst host "+ IP_l, prn=self.print_packet)
        else:
            sniff(filter="dst port " + port + " and dst host "+ IP_l, prn=self.print_packet)

    def send(self, IP_dst):
        p_tcp = Ether()/IP(dst=IP_dst)/TCP()
        p_ping = Ether()/IP()/ICMP()
        sendp(p_tcp)



if __name__ == '__main__':
    paquet1 = Paquet()
    # paquet1.capture("443","192.168.1.17")
    paquet1.send("192.168.200.1")


