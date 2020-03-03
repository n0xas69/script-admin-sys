import os


def treeSize(drive, folder):
    totalSize = 0
    filePath = os.path.join(drive, folder)
    try:
        for file in os.listdir(filePath):
            path = os.path.join(filePath, file)
            totalSize = totalSize + os.path.getsize(path)
    except:
        pass

    return totalSize


def treeDisk(disk):
    listDir = []
    for drive, dirs, files in os.walk(disk):
        for folder in dirs:
            folderPath = os.path.join(drive, folder)
            size = treeSize(drive, folder)
            size = size / 1048576
            listDir.append({"dossier" : folderPath, "taille" : size})
            listDir.sort(key=lambda x: x["taille"], reverse=True)
    topDir = listDir[:10]
    for folder in topDir:
        size = "%.2f" % folder.get("taille")
        print(folder.get("dossier") + " " + size + " Mo")
    
        

if __name__ == "__main__":
    folder = input("Entrer le chemin complet du dossier à analyser : ")
    treeDisk(folder)