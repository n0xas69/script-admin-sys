import os
import shutil as sh
import subprocess as sub

appdata = os.environ["LOCALAPPDATA"]
CHEMINS = ["C:\Windows\Temp", appdata + r"\Temp"]
Ports = [103, 104, 105, 106, 107, 108]

def delete_temp():
    for chemin in CHEMINS:
        verif_folder = os.path.exists(chemin)
        if (verif_folder == True):
            sh.rmtree(chemin,ignore_errors=True)
            try:
                os.mkdir(chemin)
            except FileExistsError:
                pass
            print(f"Le dossier {chemin} a été vidé")
        else:
            print(f"Le dossier {chemin} n'existe pas")

def firewall():
    check_firewall = sub.check_output(["whoami"])

# Appel des fonctions
delete_temp()

#test

