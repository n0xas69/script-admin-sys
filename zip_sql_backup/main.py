import os
import datetime
import shutil
import configparser
import zipfile

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
        self.sql_login = conf["SQL_login"]
        self.sql_password = conf["SQL_password"]
        self.backupD = os.path.join(self.backup_path, "Backup_D")
        self.backupW = os.path.join(self.backup_path, "Backup_W")
        self.backupM = os.path.join(self.backup_path, "Backup_M")
   
    

    # méthode qui définit dans quels dossiers faire le backup
    def location_folder(self):
        dt = datetime.datetime.today()
        backupLocation = []
        if dt.day == 1:
            backupLocation.append(self.backupM)
            backupLocation.append(self.backupD)

        elif dt.weekday == 6:
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
                os.remove(os.path.join(folder, value[0]))
                list_files = os.listdir(folder)
                nb_file = len(list_files)



    def zip_backup(self, backupLocation):
        print("backup en cours")
        if not os.path.exists(self.backupD):
            os.makedirs(self.backupD)
        if not os.path.exists(self.backupW):
            os.makedirs(self.backupW)
        if not os.path.exists(self.backupM):
            os.makedirs(self.backupM)

        if len(backupLocation) == 2:
            # Backup dans dans le dossier d'indice 0 puis copie du dossier dans l'index 1 de la liste
            zipfileToday = os.path.join(backupLocation[0], date+".zip")
            if os.path.exists(zipfileToday) == True:
                os.remove(zipfileToday)
                

            for file in os.listdir(self.data_path):
                path = os.path.join(self.data_path, file)
                with ZipFile(zipfileToday, "a") as zipf:
                    zipf.write(path)
            
            shutil.copy(zipfileToday, backupLocation[1])

        else:
            # Backup dans le dossier d'indice 0 de la liste
            zipfileToday = os.path.join(backupLocation[0], date+".zip")
            if os.path.exists(zipfileToday) == True:
                os.remove(zipfileToday)
                

            for file in os.listdir(self.data_path):
                path = os.path.join(self.data_path, file)
                with zipfile.ZipFile(zipfileToday, "a", compression=zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(path)



    def sql_backup(self):
        pass


if __name__ == "__main__":
    backup = Backup()
    backupLocation = backup.location_folder() # Suivant le jour du mois, on spécifie dans quel dossier un backup doit être fait
    backup.check_retention() # On vérifie la rétention des fichiers, on supprime les anciennes sauvegardes
    backup.zip_backup(backupLocation) # On effectue la sauvegarde des datas dans un fichier zip


