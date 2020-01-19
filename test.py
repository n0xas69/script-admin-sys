import os
import shutil as sh
import subprocess as sub


# -------------Config----------------------
appdata = os.environ["LOCALAPPDATA"]
CHEMINS = ["C:\Windows\Temp", appdata + r"\Temp"]
ports = [103,104,443,15533,10443,22000]
#------------------------------------------

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
    print("Activation du Par-Feu")
    os.system("NetSh Advfirewall set allprofiles state on")
    print("Ouverture des ports néccéssaires au bon fonctionnement de l'application.")
    for port in ports:
        os.system(f"netsh advfirewall firewall add rule name=Actibase_{port} dir=in action=allow protocol=TCP localport={port}")



# Appel des fonctions
# delete_temp()

firewall()


