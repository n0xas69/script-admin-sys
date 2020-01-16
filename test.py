import os
import shutil as sh
import subprocess as sub

CHEMINS = ["C:\Windows\Temp", r"C:\test", r"%LOCALAPPDATA%\Temp"]
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
            print("Le dossier ",chemin,"a été vidé")
        else:
            print("Le dossier ",chemin," n'existe pas")

def firewall():
    check_firewall = sub.check_output(["whoami"])

# Appel des fonctions
delete_temp()






