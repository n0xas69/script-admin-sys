"""
Utilisation de scapy pour savoir si des requêtes sur le port spécifié arrive,
création d'une classe paquet qui peut :
- envoi de paquet
- sniffage de paquet

fonction rapide d'envoi :
envoi d'une requête HTTP
envoi d'une requête DICOM
envoi d'une requête 
"""

from lib.ethernet import Ethernet

packet1 = Ethernet("kekek","lelel")
print(packet1.get_mac_dst())
print(packet1.get_mac_src())


