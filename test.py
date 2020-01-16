import os
import shutil as sh
import subprocess as sub

CHEMIN = "C:\Windows\Temp"
Ports = [103, 104, 105, 106, 107, 108]

def delete_temp():
    verif_folder = os.path.exists(CHEMIN)
    if (verif_folder == True):
        sh.rmtree(CHEMIN,ignore_errors=True)
    else:
        print("Le dossier n'existe pas")

def firewall():
    check_firewall = sub.check_output(["whoami"])
    if "Actif" in check_firewall:
        print("Le parfeu est désactivé")

# Appel des fonctions








