import os
import datetime
import shutil
import configparser

cwd = os.getcwd()
config = configparser.ConfigParser()
config.sections()
config.read(r"C:\script\PY DEV\script-admin-sys\script-admin-sys\zip_sql_backup\config.ini")
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
        # vérifie quel jour et mois on est pour la rétention jour, semaine, mois
        # Si jour = dimanche : on ajoute "day" au chemin passer en paramètre dans zip_backup
        # On liste les noms des fichiers, puis on les comptes.
        list_files = os.listdir(self.backup_path)
        if len(list_files) >= int(self.retention):
            list_fileObject = []
            for f in list_files:
                stat = (os.stat(os.path.join(self.backup_path, f))) #On récupère les infos du fichier
                list_fileObject.append({"file_name" : f, "file_date" : stat.st_atime})

            list_fileObject.sort(key=lambda x: x["file_date"])
            value = list(list_fileObject[0].values())
            os.remove(os.path.join(self.backup_path, value[0]))

        else:
            self.zip_backup()


    def zip_backup(self):
        print("backup en cours")



    def sql_backup(self):
        pass


test = Backup()
test.check_retention()
