## Fonctionnement du backup

- Vérifie quel jour on est et créer une liste de répertoire de backup
- nettoie les anciennes sauvegardes en se basant sur la rétention spécifié dans le config.ini
- effectue le backup SQL
- créer un dossier Backup_D, Backup_W, Backup_M dans le dossier backup pour gérer la rétention
- supprime le .zip du jour (si on lance 2 backup le même jour, il écrase l'ancien zip)
- effectue la copie des datas et du .bak dans un zip
- copie le zip dans les dossiers du mois ou de la semaine suivant la date du jour