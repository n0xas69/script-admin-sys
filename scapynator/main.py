from scapydou import Paquet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("sniff", help="mode capture de paquet")
parser.add_argument("send", help="mode envoi de paquet")
args = parser.parse_args()

"""
paquet1 = Paquet()
# paquet1.capture("443","192.168.1.17")
paquet1.send("192.168.1.17",1516)
"""