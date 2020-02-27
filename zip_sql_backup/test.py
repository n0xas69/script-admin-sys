import os
import pyodbc
import datetime
from main import Backup

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
error = 0
logFile = "C:\script\PY DEV\log.txt"

# tester la connexion à la base sql
def sql_test(instance):
    drivers = pyodbc.drivers()
    if "ODBC Driver 17 for SQL Server" not in drivers:
            addLog("Les Drivers ODBC ne sont pas installé")
            global error
            error += 1
    try:
        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', 
                                    server=instance, database='master', 
                                    trusted_connection='yes', autocommit=True)
        cursor = connection.cursor()
        connection.close()
    except:
        addLog("Erreur de connexion à la base SQL, vérifier l'instance sql dans le fichier config")
        error += 1

    else:
        addLog("test connexion SQL OK")


# tester l'existance du data path et du backup path
def dataPath(path):
    if os.path.isdir(path) == False:
        addLog("Le dossier data spécifié dans config.ini n'existe pas")
        global error
        error += 1


def backupPath(path):
    if os.path.isdir(path) == False:
        addLog("Le dossier backup spécifié dans config.ini n'existe pas")
        global error
        error += 1


def addLog(content):
    with open(logFile, "a") as log:
        log.write(date + " : " + content + "\n")


def delLog():
    os.remove(logFile)


def checkError(errorV):
    if errorV >= 1:
        addLog("----------- ERREUR BACKUP -------------")
    else:
        addLog("----------- BACKUP OK -------------")




