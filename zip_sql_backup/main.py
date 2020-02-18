import os
import datetime
import shutil
import configparser

config = configparser.ConfigParser()
config.sections()
config.read("C:\script\PY DEV\script-admin-sys\script-admin-sys\zip_sql_backup\config.ini")
conf = config["DEFAULT"]


date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Backup:

    def __init__(self):
        self.data_path = conf["data_path"]
        self.backup_path = conf["backup_path"]
        self.retention = conf["retention_days"]
        self.sql_instance = conf["SQL_instance"]
        self.sql_login = conf["SQL_login"]
        self.sql_password = conf["SQL_password"]
    

    def stop_process(self):
        pass


    def check_retention(self):
        """
        On liste les fichiers du path backup, tant que le nombre de backup est supérieur au nb de rétention,
        on créer une liste de dictionnaire avec pour k, v le nom du fichier et la date de création,
        on trie la liste par les valeurs des dictionnaires,
        on supprime le fichier du premier élément de la liste
        """
        
        list_files = os.listdir(self.backup_path)
        nb_file = len(list_files)
        
        while nb_file >= int(self.retention):
            list_fileObject = []
            for f in list_files:
                stat = (os.stat(os.path.join(self.backup_path, f))) #On récupère les infos du fichier
                list_fileObject.append({"file_name" : f, "file_date" : stat.st_atime})

            list_fileObject.sort(key=lambda x: x["file_date"])
            value = list(list_fileObject[0].values())
            os.remove(os.path.join(self.backup_path, value[0]))
            list_files = os.listdir(self.backup_path)
            nb_file = len(list_files)

        
        self.zip_backup()


    def zip_backup(self):
        print("backup en cours")



    def sql_backup(self):
        pass


test = Backup()
test.check_retention()
