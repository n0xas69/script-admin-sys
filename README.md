# script utile sysadmin

Dans ce repos, vous trouverez des scripts que j'ai créé pour me simplifier la vie dans mes tâches d'administrateur système, je fait en sorte que les scripts soit public donc utilisable par tout le monde.

### zip_sql_backup | progress : 50%
Script de sauvegarde. Le fichier config.ini permet de paramétrer le script. Il gère la rétention de sauvegarde et créer un dossier jour, semaine et mois pour conserver les backups. Il créer un zip contenant les datas. Gère également la sauvegarde de base SQL.

### scapynator | progress : 40%
Script qui permet de capturer les requêtes entrante sur un port spécifique, et envoyer des requêtes TCP sur une IP dst
Utilise le module scapy pour manipuler les paquets réseaux : https://scapy.net/
