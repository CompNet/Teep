# 3.1 

# Importations:
# Pour la gestion de dossiers:
from pathlib import Path
import os
# Pour la tokenization en mots:
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

# Fonction principale qui parcourt les dossiers de dossier_sortie3
def f31(dossier_sortie3,dossier_sortie3_1,dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext):
    # On va chercher le chemin de dossier_sortie3: 
    chemin = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+dossier_sortie3)
    # On va chercher dossier_sortie3
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
        # On parcourt les fichiers pour remplir la liste
        # On crée le path du sous dossier en cours:
        path_sous_dossier = Path(chemin_sous_dossier)
        # On crée un compteur qui est True si tous les fichiers ont bien bons et False sinon.
        compteur = True
        for fichier in liste_fichiers:
            # On récupère le nom du fichier sans extension:
            # Donc on veut enlever le .txt à la fin. Soit les 4 derniers caractères, soit: fichier[:-4]
            # Et qu'il faut convertier en entier
            nom_fichier = int(fichier[:-4])
            # Et on va regarder si sa valeur dans dic3 est 1 
            # On récupère la valeur dans dic3:
            valeur = dic3[nom_livre][nom_fichier]
            if valeur == 1:
                # Si c'est le cas alors:
                # On se pointe vers le fichier
                liste_fichier = path_sous_dossier.glob(fichier)
                for fichier_1 in liste_fichier:
                # On récupère le contenu
                    with open(fichier_1, "r", encoding="utf-8") as f:
                        contenu = f.read()
                # On vérifie que le contenu renvoie True par: fcontent31
                réponse = fcontent31(contenu)
                # Si oui on ne fait rien on continue: Le compteur est théoriquement toujours à True
                # Si False fait: fsupprime31 et on s'arrête là. 
                if réponse == False:
                    # On met compteur à False.
                    compteur = False
                    # On supprime le livre dans dic1, dic2, dic3 et L_nom_livres_sansext et l’ajoute à liste_mauvais_livres
                    dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext = fsupprime31(dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext, nom_livre)
                    # On fait break: On sort de la boucle. Cela réduit notre complexité. 
                    break
        # Si on a parcouru toute la liste 
        # Si compteur == True   
        if compteur == True:
            # Alors on fait: ftransfert31:
            ftransfert31(nom_livre,dossier_sortie3,dossier_sortie3_1)

    return dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext

def fcontent31(contenu):
    # on tokenize:
    tokenized_contenu = word_tokenize(contenu)
    # Nombre de mots
    n4 = len(tokenized_contenu)
    # Si moins de 20 mots on envoit False: 
    if n4 < 20:
        return False
    # Sinon on return True
    return True

# Fonction qui supprime le livre dans dic1, dic2, dic3 et L_nom_livres_sansext: fsupprime21 
# Et cette fonction l'ajoute aussi à: liste_mauvais_livres
def fsupprime31(dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext,nom_livre):
    L_nom_livres_sansext = [livre for livre in L_nom_livres_sansext if livre != nom_livre]
    liste_mauvais_livres.append("le livre respecte les normes epubs 2 et 3 mais a été écrit n'importe comment: "+nom_livre)
    dic1 = {livre: liste for livre, liste in dic1.items() if nom_livre != livre}
    dic2 = {livre: dictionnaire for livre, dictionnaire in dic2.items() if nom_livre != livre}
    dic3 = {livre: dictionnaire for livre, dictionnaire in dic3.items() if nom_livre != livre}
    return dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext

# Fonction qui transfert le dossier du livre dans dossier_sortie3_1: ftransfert3_1. Elle prend en valeur le nom du livre.
# Et les dossiers d'entrée et de sortie: dossier_sortie3,dossier_sortie3_1
def ftransfert31(nom_livre,dossier_sortie3,dossier_sortie3_1):
    # On va chercher le chemin de dossier_sortie3:
    chemin3 = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+dossier_sortie3)
    # On va chercher dossier_sortie2
    # On en extrait juste le bon dossier
    # son path:
    l_sous_dossiers3 = [f.path for f in os.scandir(chemin3) 
                        if f.is_dir() and f.name == nom_livre]
    # Mais l’écriture est mauvaise
    l_sous_dossiers3 = [ Path(d) for d in l_sous_dossiers3]
    # On parcourt tous les dossiers
    for sous_dossier3 in l_sous_dossiers3:
        # On lui crée sa version dans dossier_sortie3_1
        # Définir le chemin du dossier que vous voulez créer
        # Par exemple : "dossier_parent/nouveau_dossier"
        chemin_sous_dossier3_1 = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+dossier_sortie3_1+"/"+nom_livre)
        # Créer le dossier
        # parents=True : crée aussi les dossiers parents s'ils n'existent pas
        # exist_ok=True : ne renvoie pas d'erreur si le dossier existe déjà
        chemin_sous_dossier3_1.mkdir(parents=True, exist_ok=True)   
        # On fait une boucle for qui va parcourir le dossier dans l'ordre.
        # On récupère donc déjà tous les fichiers:
        # Chemin du sous_dossier
        chemin_sous_dossier3 = sous_dossier3
        # On en récupère la liste des fichiers:
        liste_fichiers3 = os.listdir(chemin_sous_dossier3)
        # On crée le path du sous dossier en cours:
        path_sous_dossier3 = Path(chemin_sous_dossier3)
        for fichier in liste_fichiers3:
            # On se pointe vers le fichier
            liste_fichier = path_sous_dossier3.glob(fichier)
            for fichier_1 in liste_fichier:
                # On récupère le contenu
                with open(fichier_1, "r", encoding="utf-8") as f:
                    contenu_1 = f.read()
            # Et on le remplit avec contenu:
            #chemin du dossier pas en path forcément. Mais on peut en Path. On crée un fichier dans le path: chemin_sous_dossier3_1
            #nom du fichier
            nom_fichier3 = fichier_1.name 
            chemin_complet = os.path.join(chemin_sous_dossier3_1, nom_fichier3) 
            # Le mode 'w' (write) crée le fichier s'il n'existe pas ou l'écrase s'il existe. 
            with open(chemin_complet, 'w', encoding='utf-8') as f: 
                f.write(contenu_1) 


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

# Puis la fonction totale: f31(dossier_sortie3,dossier_sortie3_1,dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext)
dic1test = {"c":[1,2],"a":[2,3],"b":[6,7]}
dic2test = {"c":{1:[1,2],2:[1,2]},"a":{1:[1,2]},"b":{1:[1,2]}}
dic3test = {"c":{1:1,2:0},"a":{1:0,2:1},"b":{1:0}}
liste_mauvais_livrestest = ["d"]
L_nom_livres_sansexttest = ["a","b","c"] 
print(dic1test, dic2test, dic3test, liste_mauvais_livrestest, L_nom_livres_sansexttest)
dic1test, dic2test, dic3test, liste_mauvais_livrestest, L_nom_livres_sansexttest = f31("dossier_sortie3test","dossier_sortie31test",dic1test, dic2test, dic3test, liste_mauvais_livrestest, L_nom_livres_sansexttest)
print(dic1test, dic2test, dic3test, liste_mauvais_livrestest, L_nom_livres_sansexttest)
# On est censé obtenir en sortie: dans dossier_sortie3_1: le a et le b mais pas le c, que l'on est censé retrouver dans liste_mauvais_livrestest
# fsupprime31 n'a pas été réalisée. 
# C'est bon le test marche. 
"""
