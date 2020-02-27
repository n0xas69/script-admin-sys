import os
import datetime
import shutil
import configparser
import zipfile
import pyodbc
import test

cwd = os.getcwd()
config = configparser.ConfigParser()
config.sections()
config.read("C:\script\PY DEV\script-admin-sys\script-admin-sys\zip_sql_backup\config.ini")
conf = config["DEFAULT"]

date = datetime.datetime.now().strftime("%Y-%m-%d")

class Backup:

    def __init__(self):
        self.data_path = conf["data_path"]
        self.backup_path = conf["backup_path"]
        self.retention = conf["retention_days"]
        self.sql_instance = conf["SQL_instance"]
        self.sql_database = conf["SQL_database"]
        self.backupD = os.path.join(self.backup_path, "Backup_D")
        self.backupW = os.path.join(self.backup_path, "Backup_W")
        self.backupM = os.path.join(self.backup_path, "Backup_M")
   
    
    # méthode qui définit dans quels dossiers faire le backup
    def location_folder(self):
        dt = datetime.datetime.today()
        backupLocation = []
        if dt.day == 1: # Si on est le premier jour du mois
            backupLocation.append(self.backupM)
            backupLocation.append(self.backupD)

        elif dt.weekday() == 6: # Si on est dimanche
            backupLocation.append(self.backupW)
            backupLocation.append(self.backupD)

        else:
            backupLocation.append(self.backupD)
        return backupLocation
  

    def stop_process(self):
        pass


    def check_retention(self):
        """
        On liste les fichiers du path backup, tant que le nombre de backup est supérieur au nb de rétention,
        on créer une liste de dictionnaire avec pour k, v le nom du fichier et la date de création,
        on trie la liste par les valeurs des dictionnaires,
        on supprime le fichier du premier élément de la liste
        """
        if not os.path.exists(self.backupD):
            os.makedirs(self.backupD)
        if not os.path.exists(self.backupW):
            os.makedirs(self.backupW)
        if not os.path.exists(self.backupM):
            os.makedirs(self.backupM)

        checkFolder = [self.backupD, self.backupW, self.backupM]

        for folder in checkFolder:
            list_files = os.listdir(folder)
            nb_file = len(list_files)
            
            while nb_file > int(self.retention):
                list_fileObject = []
                for f in list_files:
                    stat = (os.stat(os.path.join(folder, f))) #On récupère les infos du fichier
                    list_fileObject.append({"file_name" : f, "file_date" : stat.st_atime})

                list_fileObject.sort(key=lambda x: x["file_date"])
                value = list(list_fileObject[0].values())
                try:
                    os.remove(os.path.join(folder, value[0]))
                except:
                    test.addLog("Impossible de supprimer l'ancienne sauvegarde " + folder)
                    test.error += 1
                list_files = os.listdir(folder)
                nb_file = len(list_files)


    def zip_backup(self, backupLocation, sqlBackup):
        print("backup en cours")
        
        if len(backupLocation) == 2:
            # Backup dans dans le dossier d'indice 0 puis copie du dossier dans l'index 1 de la liste
            zipfileToday = os.path.join(backupLocation[0], date+".zip")
            if os.path.exists(zipfileToday) == True:
                os.remove(zipfileToday)
                

            # On parcours le dossier data, pour chaque fichier dans la liste renvoyé par os.walk, on l'ajoute au zip
            for base, dirs, files in os.walk(self.data_path):    
                for file in files:
                    path = os.path.join(base, file)
                    with zipfile.ZipFile(zipfileToday, "a", compression=zipfile.ZIP_DEFLATED) as zipf:
                        zipf.write(path)
            with zipfile.ZipFile(zipfileToday, "a", compression=zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(sqlBackup)
            shutil.copy(zipfileToday, backupLocation[1])

        else:
            # Backup dans le dossier d'indice 0 de la liste
            zipfileToday = os.path.join(backupLocation[0], date+".zip")
            if os.path.exists(zipfileToday) == True:
                os.remove(zipfileToday)

            for base, dirs, files in os.walk(self.data_path):    
                for file in files:
                    path = os.path.join(base, file)
                    with zipfile.ZipFile(zipfileToday, "a", compression=zipfile.ZIP_DEFLATED) as zipf:
                        zipf.write(path)
            with zipfile.ZipFile(zipfileToday, "a", compression=zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(sqlBackup)

        os.remove(sqlBackup)


    def sql_backup(self):
        drivers = pyodbc.drivers()
        backup = r"C:\Windows\Temp\jfse.bak"
        if "ODBC Driver 17 for SQL Server" not in drivers:
            print("Les Drivers ODBC ne sont pas installé")

        connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', 
                                server=self.sql_instance, database='master', 
                                trusted_connection='yes', autocommit=True)
        cursor = connection.cursor()
        cursor.execute("BACKUP DATABASE [" + self.sql_database + "] TO  DISK = N'"+ backup + "' WITH NOFORMAT, NOINIT,  NAME = N'" + self.sql_database + "-Complète Base de données Sauvegarde', SKIP, NOREWIND, NOUNLOAD,  STATS = 10")
        while cursor.nextset():
            pass
        connection.close()
        return backup



if __name__ == "__main__":
    backup = Backup()
    test.delLog() # On vérifie si un fichier log est présent, si oui on le supprime
    test.sql_test(backup.sql_instance) # On vérifie la connexion à la BDD
    test.dataPath(backup.data_path) # On vérifie le chemin des données
    test.backupPath(backup.backup_path) # On vérifie le chemin destination des backup
    backupLocation = backup.location_folder() # Suivant le jour du mois, on spécifie dans quel dossier un backup doit être fait
    backup.check_retention() # On vérifie la rétention des fichiers, on supprime les anciennes sauvegardes
    test.addLog("----------- DEBUT BACKUP -------------")
    sqlBackup = backup.sql_backup() # On effectue un .bak de la base
    backup.zip_backup(backupLocation, sqlBackup) # On effectue la sauvegarde des datas dans un fichier zip
    test.checkError(test.error) # On vérifie si il y a eu des erreurs



