# 2.1 

# Importations:
# Pour la gestion de dossiers:
from pathlib import Path
import os
# Pour le tri naturel
from natsort import natsorted

# Fonction principale qui parcourt les dossiers de dossier_sortie2
def f21(dossier_sortie2,dossier_sortie3,dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext):
    # On va chercher le chemin de dossier_sortie2: 
    chemin = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+dossier_sortie2)
    # On va chercher dossier_sortie2
    # On en extrait tous les dossiers
    # Les paths
    l_sous_dossiers = [f.path for f in os.scandir(chemin) if f.is_dir()]
    # les noms:
    l_noms_sous_dossiers = [f.name for f in os.scandir(chemin) if f.is_dir()]
    # Mais l’écriture est mauvaise
    l_sous_dossiers = [ Path(d) for d in l_sous_dossiers]
    # On parcourt tous les dossiers
    for k in range(len(l_sous_dossiers)):
        # Pour chaque dossier:
        # Son path:
        sous_dossier = l_sous_dossiers[k]
        # Son nom:
        nom_livre = l_noms_sous_dossiers[k]
        print(nom_livre)
        # On fait une boucle for qui va parcourir le dossier dans l'ordre.
        # On récupère donc déjà tous les fichiers
        # Chemin du sous_dossier
        chemin_sous_dossier = sous_dossier
        # On en récupère la liste des fichiers:
        liste_fichiers = os.listdir(chemin_sous_dossier)
        # On trie cette liste
        liste_fichiers = natsorted(liste_fichiers)
        # On met les contenus dans une liste.
        # La liste:
        l_contenus = []
        # On parcourt les fichiers pour remplir la liste
        # On crée le path du sous dossier en cours:
        path_sous_dossier = Path(chemin_sous_dossier)
        for fichier in liste_fichiers:
            # On se pointe vers le fichier
            liste_fichier = path_sous_dossier.glob(fichier)
            for fichier_1 in liste_fichier:
            # On récupère le contenu
                with open(fichier_1, "r", encoding="utf-8") as f:
                    contenu = f.read()
                # on le met dans la liste
            l_contenus.append(contenu)
        # on met le compteur à True
        compteur = True
        # On parcourt la liste l_contenus jusqu'au range de len(liste)-2
        for k in range(len(l_contenus)-2):
            # On regarde si le contenu est égal aux deux contenus suivant.
            if l_contenus[k] == l_contenus[k+1] == l_contenus[k+2] and fvide21(l_contenus[k]):
                # Si c'est le cas:
                dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext,nom_livre = fsupprime21(dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext,nom_livre)
                # Et on met le compteur à False car alors il ne fait pas transférer ce livre
                compteur = False
                # Et alors on sort de la boucle afin de réduire la complexité
                break
        # Si on a tout parcouru sans que rien n'arrive alors on peut transférer sinon on ne fait rien: 
        # Si on a parcouru toute la liste 
        # Si compteur == True   
        if compteur == True:
            # Alors on fait: ftransfert31:
            ftransfert21(nom_livre,dossier_sortie2,dossier_sortie3)
    return dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext
            

# Fonction qui détecte si le fichier est vide: fvide21. 
# Retourne True si le fichier n'est pas vide.
def fvide21(contenu):
    if contenu == "":
        return False
    return True

# Fonction qui supprime le livre dans dic1, dic2 et L_nom_livres_sansext: fsupprime21 
# Et cette fonction l'ajoute aussi à: liste_mauvais_livres
def fsupprime21(dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext,nom_livre):
    L_nom_livres_sansext = [livre for livre in L_nom_livres_sansext if livre != nom_livre]
    liste_mauvais_livres.append("le livre respecte les normes epubs 2 et 3 mais a été écrit n'importe comment: "+nom_livre)
    dic1 = {livre: liste for livre, liste in dic1.items() if nom_livre != livre}
    dic2 = {livre: dictionnaire for livre, dictionnaire in dic2.items() if nom_livre != livre}
    return dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext,nom_livre

# Fonction qui transfert le dossier du livre dans dossier_sortie3: ftransfert21. Elle prend en valeur le nom du livre.
# Et les dossiers d'entrée et de sortie: dossier_sortie2,dossier_sortie3
def ftransfert21(nom_livre2,dossier_sortie2,dossier_sortie3):
    # On va chercher le chemin de dossier_sortie2: 
    chemin2 = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+dossier_sortie2)
    # On va chercher dossier_sortie2
    # On en extrait juste le bon dossier
    # son path:
    l_sous_dossiers2 = [f.path for f in os.scandir(chemin2) 
                        if f.is_dir() and f.name == nom_livre2]
    # Mais l’écriture est mauvaise
    l_sous_dossiers2 = [ Path(d) for d in l_sous_dossiers2]
    # On parcourt tous les dossiers
    for sous_dossier2 in l_sous_dossiers2:
        # On lui crée sa version dans dossier_sortie3
        # Définir le chemin du dossier que vous voulez créer
        # Par exemple : "dossier_parent/nouveau_dossier"
        chemin_sous_dossier3 = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+dossier_sortie3+"/"+nom_livre2)
        # Créer le dossier
        # parents=True : crée aussi les dossiers parents s'ils n'existent pas
        # exist_ok=True : ne renvoie pas d'erreur si le dossier existe déjà
        chemin_sous_dossier3.mkdir(parents=True, exist_ok=True)   
        # On fait une boucle for qui va parcourir le dossier dans l'ordre.
        # On récupère donc déjà tous les fichiers:
        # Chemin du sous_dossier
        chemin_sous_dossier2 = sous_dossier2
        # On en récupère la liste des fichiers:
        liste_fichiers2 = os.listdir(chemin_sous_dossier2)
        # On crée le path du sous dossier en cours:
        path_sous_dossier2 = Path(chemin_sous_dossier2)
        for fichier in liste_fichiers2:
            # On se pointe vers le fichier
            liste_fichier = path_sous_dossier2.glob(fichier)
            for fichier_1 in liste_fichier:
                # On récupère le contenu
                with open(fichier_1, "r", encoding="utf-8") as f:
                    contenu = f.read()
            # Et on le remplit avec contenu:
            #chemin du dossier pas en path forcément. Mais on peut en Path. On crée un fichier dans le path: chemin_sous_dossier3
            #nom du fichier
            nom_fichier2 = fichier_1.name 
            chemin_complet = os.path.join(chemin_sous_dossier3, nom_fichier2) 
            # Le mode 'w' (write) crée le fichier s'il n'existe pas ou l'écrase s'il existe. 
            with open(chemin_complet, 'w', encoding='utf-8') as f: 
                f.write(contenu) 


"""TESTS:
# On teste la fonction
# On teste d'abord: ftransfert21(nom_livre2,dossier_sortie2,dossier_sortie3):
# ftransfert21("_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley","dossier_test2","dossier_test3")
# C'est bon elle marche

# Puis: fsupprime21(dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext,nom_livre)
dic1test = {"_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley":[1,2],"a":[2,3],"b":[6,7]}
dic2test = {"_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley":{1:[1,2]},"a":{1:[1,2]},"b":{1:[1,2]}}
liste_mauvais_livrestest = ["d"]
L_nom_livres_sansext = ["a","b","_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley"]
nom_livre = "_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley"
print(fsupprime21(dic1test,dic2test,liste_mauvais_livrestest,L_nom_livres_sansext,nom_livre))
# C'est bon elle marche

# Puis la fonction totale: f21(dossier_sortie2,dossier_sortie3,dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext)
dic1test = {"_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley":[1,2],"a":[2,3],"b":[6,7]}
dic2test = {"_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley":{1:[1,2]},"a":{1:[1,2]},"b":{1:[1,2]}}
liste_mauvais_livrestest = ["d"]
L_nom_livres_sansexttest = ["a","b","_OceanofPDF.com_The_War_I_Finally_Won_-_Kimberly_Brubaker_Bradley"] 
f21("dossier_sortie2test","dossier_sortie3test",dic1test, dic2test, liste_mauvais_livrestest, L_nom_livres_sansexttest)
# Ca marche
# On appelle cette fonction dans total.py? Et on modifie total.py concernant dossier_sortie3.
# On refait le canva avec ces fonctions
"""