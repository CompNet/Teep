# Test: Fichier de test pour tester
# T à la fin des variables

# Importations
# Pour la gestion de fichiers et de dossiers:
import os
from pathlib import Path 
# Pour le graphique
import matplotlib.pyplot as plt
import numpy as np
# Pour tri naturel:
from natsort import natsorted

# On note le L_nom_livres_erreures
# Pour éviter d'avoir à relancer tout le traitement à chaque fois
L_nom_livres_erreures = ["Father_goriot", "Grave Witch (Alex Craft, #01) -- Price, Kalayna -- Alex Craft 1, 2010 -- Penguin Group (USA) --", 
"The Enchanted Castle by E. Nesbit", "_OceanofPDF.com_The_Winter_of_Our_Discontent_-_John_Steinbeck", 
"_OceanofPDF.com_Under_the_Never_Sky_Omnibus_-_Veronica_Rossi",
"_OceanofPDF.com_Wuthering_Heights_-_Emily_Bronte (1)", "_OceanofPDF.com_Yellow_Crocus_-_Laila_Ibrahim", 
"The_Martian_by_Andy_Weir", "_OceanofPDF.com_True_love_experiment_-_Christina_Lauren", 
"_OceanofPDF.com_Twisted_-_Emily_McIntire", "_OceanofPDF.com_Wicked_and_the_Wallflower_-_Sarah_MacLean"]


# Fonction fT1
# Fonction qui calcule pour chaque livre:
# Pour chaque fichier qui sont effectivement des chapitres combien en avait-t-on trouver
def fT1():
    # On remet dictest_1 à {}
    dictest_1 = {}
    # On parcourt les dossiers du dossier annoté. 
    # On récupère la liste des paths des sous dossiers du dossier annoté.
    # Chemin du dossier où il y a les sous dossiers
    dossier_parentT = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/Jeu de données que l'on devrait obtenir en sortie")
    # Utilisation de os.scandir pour aller dans le dossier parent et ne récupérer que ce qui est un dossier: 
    #.is_dir().
    #On obtient alors la liste des paths des sous dossiers: 
    sous_dossiers_pathT = [fT.path for fT in os.scandir(dossier_parentT) if fT.is_dir()]
    #On obtient alors la liste des noms des sous dossiers: 
    sous_dossiers_nameT = [fT_1.name for fT_1 in os.scandir(dossier_parentT) if fT_1.is_dir()]
    #mais l’écriture est mauvaise pour les paths. Il faut la refaire: 
    sous_dossiers_pathT = [ Path(dT) for dT in sous_dossiers_pathT]
    # On parcourt les livres de sous_dossiers_pathT
    for k in range(len(sous_dossiers_pathT)):
        # Pour chaque dossier:
        # On crée sa clé dans dictest_1 et le sous dictionnaire associé. 
        # On récupère le nom du sous dossier
        nameT = sous_dossiers_nameT[k]
        # On vérifie qu'elle n'est pas dans: L_nom_livres_erreures
        if nameT not in L_nom_livres_erreures:
            # On dit qu'on y est:
            print(nameT)
            # On créer sa clé:
            dictest_1[nameT] = {}
            # On le parcourt. On en récupère tous les fichiers du dossier:
            # On récupère le path du dossier:
            dossier_atuelT = sous_dossiers_pathT[k]
            # On en récupère tous les fichiers textes
            # On en a une liste: 
            fichiersT = os.listdir(dossier_atuelT)
            # On la parcourt:
            for fichierT in fichiersT: 
                # Pour chaque fichier
                # On récupère son contenu:
                # On récupère le fichier avec un .glob sur le dossier et son nom: fichierT
                fichierT_1 = dossier_atuelT.glob(fichierT)
                for fichierT_2 in fichierT_1:
                    with open(fichierT_2, "r", encoding="utf-8") as fT_2:
                        contenuT = fT_2.read()
                # On va dans le dossier associé dans le dossier non annoté. 
                # On en créer le chemin:
                chemin_non_annotéT = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_sortie4/"+nameT)
                # On va récupérer tous les noms de fichiers sans extensions. 
                # On va ensuite les trier sans extension. 
                # Afin de les parcourir dans l'ordre croissant. 
                # Puis on les récréera plus tard avec leurs extensions.
                # Afin d'avoir leurs contenus. 
                fichiers_non_annotéT = chemin_non_annotéT.glob("*.txt")
                # On en récupère que les noms pas les extensions afin ensuite de pouvoir les trier comme des chiffres: 
                fichiers_non_annotéT = [nom_avec_extT.stem for nom_avec_extT in fichiers_non_annotéT]
                # On initialise aT à 0:
                aT = 0
                # On va essayer de voir si on le retrouve bien dans le dossier des résultats 
                for fichier_non_annotéT in fichiers_non_annotéT:
                    # On recréer le fichier plus tard avec son extension.
                    # Afin d'avoir leurs contenus. 
                    # On regarde si on trouve le contenu dans un des fichiers.
                    # On récupère le contenu du fichier non annoté: 
                    # On récupère le fichier avec un .glob sur le dossier et son nom: fichierT
                    fichier_non_annotéT_1 = chemin_non_annotéT.glob(fichier_non_annotéT+".txt")
                    for fichier_non_annotéT_2 in fichier_non_annotéT_1:
                        with open(fichier_non_annotéT_2, "r", encoding="utf-8") as fT_3:
                            contenuT_1 = fT_3.read()
                    if contenuT == contenuT_1:
                        aT = 1
                # On met aT dans dictest_1
                # On récupère le nom du fichier avec extension parce que l'on s'en fiche avec ou sans: 
                name_fileT = fichierT
                dictest_1[nameT][name_fileT] = aT
    
    return dictest_1

print(fT1())

# Fonction fT2
# Fonction qui calcule pour chaque livre:le nombre de fichiers que l'on a trouvé.
def fT2():
    # On remet dictest_2 à {}
    dictest_2 = {}
    # On parcourt les dossiers du dossier annoté. 
    # On récupère la liste des paths des sous dossiers du dossier trouvé.
    # Chemin du dossier où il y a les sous dossiers
    dossier_parentT = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_sortie4")
    # Utilisation de os.scandir pour aller dans le dossier parent et ne récupérer que ce qui est un dossier: 
    #.is_dir().
    #On obtient alors la liste des paths des sous dossiers: 
    sous_dossiers_pathT = [fT.path for fT in os.scandir(dossier_parentT) if fT.is_dir()]
    #On obtient alors la liste des noms des sous dossiers: 
    sous_dossiers_nameT = [fT_1.name for fT_1 in os.scandir(dossier_parentT) if fT_1.is_dir()]
    #mais l’écriture est mauvaise pour les paths. Il faut la refaire: 
    sous_dossiers_pathT = [ Path(dT) for dT in sous_dossiers_pathT]
    # On parcourt les livres de sous_dossiers_pathT
    for k in range(len(sous_dossiers_pathT)):
        # Pour chaque dossier:
        # On crée sa clé dans dictest_2 et le sous dictionnaire associé. 
        # On récupère le nom du sous dossier
        nameT = sous_dossiers_nameT[k]
        # On vérifie qu'elle n'est pas dans: L_nom_livres_erreures
        if nameT not in L_nom_livres_erreures:
            # On dit qu'on y est:
            print(nameT)
            # On le parcourt. On en récupère tous les fichiers du dossier:
            # On récupère le path du dossier:
            dossier_atuelT = sous_dossiers_pathT[k]
            # On en récupère tous les fichiers textes
            # On en a une liste: 
            fichiersT = os.listdir(dossier_atuelT)
            # On créer sa clé: Le nombre de fichiers que l'on a dans le dossier
            dictest_2[nameT] = len(fichiersT)
    
    return dictest_2


# On va calculer la précision le rappel et le F score pour chaque livre mais aussi
# Pour tous les livres. 
# On a que des relations linéaires il suffira de faire la moyenne des autres.
# Fonction de création de la précision du rappel et du fscore:
def fmétriques(dictest1,dictest2):
    # Liste des rappels
    L_rappels = []
    # Liste des précisions
    L_précisions = []
    # Liste des f scores
    L_fscores = []
    # Absisse:
    # Liste des livres: clésT
    # On parcourt dictest1:
    # On récupère toutes ses clés
    clésT = list(dictest1.keys())
    # Nombre de livres total:
    nb_livre = len(clésT)
    # On les parcourt:
    for cléT in clésT:
        # Pour chaque livre:
        print(cléT)
        # Les rappels:
        # On parcourt les fichiers, donc ses clés:
        sous_clésT = dictest1[cléT].keys()
        # Le nombre de fichiers que l’on a bien retrouvé
        nb_file_brT = 0
        # Le nombre de fichiers en tout.
        nb_fileT = len(sous_clésT)
        # On les parcourt:
        for sous_cléT in sous_clésT:
            # On récupère les valeurs:
            aT = dictest1[cléT][sous_cléT]
            if aT == 1:
                nb_file_brT += 1
        # On a alors le rappel:
        rappel = nb_file_brT/nb_fileT
        
        # Pour les précisions:
        # On parcourt les fichiers, donc ses clés:
        # On a le nombre de fichiers que l'on attribué à chapitres pour ce livre:
        nb_files = dictest2[cléT]
        # On a alors la précision
        précision = nb_file_brT/nb_files

        # Pour les F score:
        if précision+rappel != 0:
            f_score = 2*((précision*rappel)/(précision+rappel))
        else:
            f_score = 0
        
        # On les ajoute aux listes:
        # Liste des rappels
        L_rappels.append(rappel)
        # Liste des précisions
        L_précisions.append(précision)
        # Liste des f scores
        L_fscores.append(f_score)
    
    # Initialisation des totaux:
    total_rappel = 0
    total_précision = 0
    total_f_score = 0
    # Les rappels, précisions et f score totaux:
    for k in range(nb_livre):
        total_rappel += L_rappels[k]
        total_précision += L_précisions[k]
        total_f_score += L_fscores[k]
    rappel_total = total_rappel/nb_livre
    précision_totale = total_précision/nb_livre
    f_score_total = total_f_score/nb_livre

    return L_rappels, L_précisions, L_fscores, rappel_total, précision_totale, f_score_total


# Test
# On a donc: avec dictest1 de fT1: le nombre de documents correctement attribué comme chapitre.
# Et en faisant le len des clés de chaque livre on a le nombre d'éléments:
# Qui doivent être attribué comme chapitre. 
# Et avec: dictest2 de fT2: le nombre d'éléments que l'on attribué comme chapitres
# dictest1 = fT1()
# dictest2 = fT2()
#L_rappels, L_précisions, L_fscores, rappel_total, précision_totale, f_score_total = fmétriques(dictest1,dictest2)
#print(L_rappels, L_précisions, L_fscores, rappel_total, précision_totale, f_score_total)


# Fonction de détection de l'ordre.
# On va mettre en place la corrélation de Kendall. Car c'est la plus précise et surtout elle marche mieux avec les petits échantillons.
# On va pour chaque livre transformer les contenus en ordres.
# Pour chaque livre on va vouloir donc une liste de nombres croissant 0,1,2,3..: l1. On part de 0.
# Qui correspond à la liste des fichiers annotés que l'on considère qu'ils ont été mis dans le bon ordre. 
# Et on va alors créer la liste des nombres qui correspond aux fichiers que nous on a produit: l2. I.e. pour chaque contenu de fichier produit:
# On regarde quelle est sa valeur dans la liste l1. Et on la note dans l2. C'est ainsi que l'on crée la deuxième liste.
# Si on ne trouve pas le fichier dans les fichiers annotés: c'est pas grave on ne va pas ici considérer les faux positifs.
# Fonction: fcréationl
# Il faut refaire la fonction. Il faut pour chaque livre créer l1 et l2 en fonction de l'univers donc de l1.
# Il faut donc retravailler l2. Il faut la créer de la même taille que l1. Il faut parcourir le dossier annoté. 
# On va parcourir l1. Et on regarde si pour cet indice pour le fichier annoté on trouve ce fichier.
# Il faut que pour chaque indice de l2 qui correspond donc à un fichier annoté avoir soit 0 si le fichier n'existe pas soit son rang.
def fcréationl():
    # On crée dictest3. Qui a comme clés les livres. Et comme valeur. Une liste de liste.
    # Avec dedans l1: la liste pour le dossier annoté du livre et l2 pour celui produit par le programme.
    dictest_3 = {}
    # On parcourt les dossiers du dossier annoté. 
    # On récupère la liste des paths des sous dossiers du dossier trouvé.
    # Chemin du dossier où il y a les sous dossiers
    dossier_parentT = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/Jeu de données que l'on devrait obtenir en sortie")
    # Utilisation de os.scandir pour aller dans le dossier parent et ne récupérer que ce qui est un dossier: 
    #.is_dir().
    #On obtient alors la liste des paths des sous dossiers: 
    sous_dossiers_pathT = [fT.path for fT in os.scandir(dossier_parentT) if fT.is_dir()]
    #On obtient alors la liste des noms des sous dossiers: 
    sous_dossiers_nameT = [fT_1.name for fT_1 in os.scandir(dossier_parentT) if fT_1.is_dir()]
    #mais l’écriture est mauvaise pour les paths. Il faut la refaire: 
    sous_dossiers_pathT = [ Path(dT) for dT in sous_dossiers_pathT]
    # On parcourt les livres de sous_dossiers_pathT
    for k in range(len(sous_dossiers_pathT)):
        # Pour chaque dossier:
        # On crée sa clé dans dictest_1 et le sous dictionnaire associé. 
        # On récupère le nom du sous dossier
        nameT = sous_dossiers_nameT[k]
        # On vérifie qu'elle n'est pas dans: L_nom_livres_erreures
        if nameT not in L_nom_livres_erreures:
            # On dit qu'on y est:
            print(nameT)
            # On créer sa clé:
            dictest_3[nameT] = []
            # On le parcourt. On en récupère tous les fichiers du dossier:
            # On récupère le path du dossier:
            dossier_atuelT = sous_dossiers_pathT[k]
            # On en récupère tous les fichiers textes
            # On en a une liste: 
            fichiersT = os.listdir(dossier_atuelT)
            # On trie cette liste dans l'ordre croissant:
            # On enlève l'extension i.e. les 4 derniers caractères. Car on a que des fichiers .txt. 
            fichiersT = [f[:-4] for f in fichiersT]
            # On trie la liste
            fichiersT = natsorted(fichiersT)
            # On crée la liste l1 du livre:
            # On crée l1. Qui va de 0 à la taille de la liste fichiersT. Cra c'est la liste qui est de taille l'univers. L'univers qui est l'ensemble des fichiers.
            # Du dossier annoté donc: fichiersT.
            l1 = list(range(len(fichiersT)))
            # Et la lite l2:
            # Il faut que pour chaque indice de l2 qui correspond donc à un fichier annoté avoir soit -10 si le fichier n'existe pas soit son rang.
            l2 = [-10 for k in range(len(fichiersT))]
            # On la parcourt:
            # On va parcourir l1. Et on regarde si pour cet indice pour le fichier annoté on trouve ce fichier.
            for k1 in range(len(fichiersT)): 
                fichierT = fichiersT[k1]
                # Pour chaque fichier
                # On récupère son contenu:
                # On récupère le fichier avec un .glob sur le dossier et son nom: fichierT
                fichierT_1 = dossier_atuelT.glob(fichierT+".txt")
                for fichierT_2 in fichierT_1:
                    with open(fichierT_2, "r", encoding="utf-8") as fT_2:
                        contenuT = fT_2.read()
                # On va dans le dossier associé dans le dossier non annoté. 
                # On en créer le chemin:
                chemin_non_annotéT = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_sortie4/"+nameT)
                # On va récupérer tous les noms de fichiers sans extensions. 
                # On va ensuite les trier sans extension. 
                # Afin de les parcourir dans l'ordre croissant. 
                # Puis on les récréera plus tard avec leurs extensions.
                # Afin d'avoir leurs contenus. 
                fichiers_non_annotéT = chemin_non_annotéT.glob("*.txt")
                # On en récupère que les noms pas les extensions afin ensuite de pouvoir les trier comme des chiffres: 
                fichiers_non_annotéT = [nom_avec_extT.stem for nom_avec_extT in fichiers_non_annotéT]
                # On trie cette liste dans l'ordre croissant:
                fichiers_non_annotéT = natsorted(fichiers_non_annotéT)
                # On initialise le pas b à 0:
                b = 0
                # On va essayer de voir si on le retrouve bien dans le dossier des non annotés
                for fichier_non_annotéT in fichiers_non_annotéT:
                    # On recréer le fichier plus tard avec son extension.
                    # Afin d'avoir leurs contenus. 
                    # On regarde si on trouve le contenu dans un des fichiers.
                    # On récupère le contenu du fichier annoté: 
                    # On récupère le fichier avec un .glob sur le dossier et son nom: fichierT
                    fichier_non_annotéT_1 = chemin_non_annotéT.glob(fichier_non_annotéT+".txt")
                    for fichier_non_annotéT_2 in fichier_non_annotéT_1:
                        with open(fichier_non_annotéT_2, "r", encoding="utf-8") as fT_3:
                            contenuT_1 = fT_3.read()
                    # On regarde si il s'agit du fichier que l'on cherche.
                    # On va parcourir l1. Et on regarde si pour cet indice pour le fichier annoté on trouve ce fichier.
                    if contenuT == contenuT_1:
                        # Si oui. On met alors b dans l2. 
                        l2[k1] = b
                        # Et on arrête la boucle ici. 
                        break
                    # On ajoute 1 à b si le if n'a pas été réalisé et donc il faut continuer de parcourir les fichiers. 
                    b += 1
                    # Si in fine on ne trouve pas ce fichier dans les fichiers annotés c'est qu'il s'agissait d'un faux positif et donc on l'a enlevé on a bien fait. 
            # On ajoute les deux listes au dictionnaires pour ce livre. 
            dictest_3[nameT] = [l1,l2]
    
    return dictest_3


# On va faire: le principe du kendall généralisé pour Emond & Mason.
# Car le principe du kendall généralisé : permet de comparer des listes classées. 
# Et : pour Emond & Mason : permet de le faire avec des ex eaquos dans les listes ou avec une liste plus courte que l'autre. 
# Cette méthode se fait pour des listes décroissantes généralement, l = [a,b,c] où a > b > c. 
# Nous on va le faire pour des listes décroissantes. 

# On fait la corrélation de kendall pour chaque livre. 
# On appelle la fonction: fKendall(dictest_3)
def fKendall(dictest_3):
    # On parcourt dictest_3
    clés = dictest_3.keys() 
    # Liste des taus:
    L_taus = []
    # On en parcourt les livres 
    for clé in clés:
        print(clé)
        # Pour chaque livre : on en récupère l1 et l2
        l1 = dictest_3[clé][0]
        l2 = dictest_3[clé][1]
        #print(l1)
        #print(l2)
        # On crée l'univers. Donc la liste de tous les éléments possibles dans les deux listes. Donc l1 en fait. 
        univers = l1
        # On crée les deux matrices
        # deux listes de listes 
        # Pour chaque liste: on l'a remplit de liste pour k in range(len(univers)). Et dans chaque sous liste on met 0 pour k in range(len(univers)).
        # L'avantage de jouer avec les listes c'est qu'ici les indices de nos matrices sont nos valeurs de notre univers. 
        matrice1 = [[0 for k in range(len(univers))]for k in range(len(univers))]
        matrice2 = [[0 for k in range(len(univers))]for k in range(len(univers))]
        # On parcourt alors chaque matrice et on la remplit avec les bonnes valeurs.
        # Pour la matrice1
        # On parcourt chaque ligne. Donc chaque liste de matrice1. Avec k1.
        for k1 in range(len(matrice1)):
            # Pour chaque ligne on garde la valeur de cette ligne dans l1. La valeur que l'on a pour l'indice de cette ligne.
            valeur_ligne = l1[k1]
            # Et alors on parcourt les indices de la ligne. Avec k2. La ligne: matrice1[k1]
            for k2 in range(len(matrice1[k1])):
                # Pour chacun des indices on va chercher la valeur correspondante dans l1. 
                valeur_colonne = l1[k2]
                # Si k1 == k2: On met 0 dans matrice1[k1][k2]. Car alors nous sommes sur la diagonale. 
                if k1 == k2:
                    matrice1[k1][k2] = 0
                else:
                    # On rappelle: que l'on fait comme le principe du kendall généralisé pour Emond & Mason sauf en inversé pour les > et <.
                    # Car nous sommes sur une liste décroissante. 
                    # Si cette valeur est supérieure ou égale à notre valeur. On met 1 dans matrice1[k1][k2]
                    if valeur_colonne >= valeur_ligne:
                        matrice1[k1][k2] = 1
                    # Si cette valeur est strictement inférieure à notre valeur. On met -1 dans matrice1[k1][k2]
                    if valeur_colonne < valeur_ligne:
                        matrice1[k1][k2] = -1

        # Pour la matrice2
        # On parcourt chaque ligne. Donc chaque liste de matrice2. Avec k1_1.
        for k1_1 in range(len(matrice2)):
            # Pour chaque ligne on garde la valeur de cette ligne dans l2. La valeur que l'on a pour l'indice de cette ligne.
            valeur_ligne_1 = l2[k1_1]
            # Si la valeur est -10 c'est que de base on n'a rien pour cet indice il faut donc mettre des 0 partout sur 
            # Sa ligne et sa colonne:
            # Pour sa ligne: 
            if valeur_ligne_1 == -10:
                matrice2[k1_1] = [0 for k in range(len(matrice2[k1_1]))]
            else:
                # Et alors on parcourt les indices de la ligne. Avec k2. La ligne: matrice2[k1_1]
                for k2_1 in range(len(matrice2[k1_1])):
                    # Pour chacun des indices on va chercher la valeur correspondante dans l2. 
                    valeur_colonne_1 = l2[k2_1]
                    # Si k1_1 == k2_1: On met 0 dans matrice2[k1_1][k2_1]. Car alors nous sommes sur la diagonale. 
                    if k1_1 == k2_1:
                        matrice2[k1_1][k2_1] = 0
                    else:
                        # Si la valeur est -10 c'est que de base on n'a rien pour cet indice il faut donc mettre des 0 partout sur 
                        # Sa ligne et sa colonne:
                        # Pour sa colonne:
                        if valeur_colonne_1 == -10:
                            matrice2[k1_1][k2_1] = 0
                        else:
                            # On rappelle: que l'on fait comme le principe du kendall généralisé pour Emond & Mason sauf en inversé pour les > et <.
                            # Car nous sommes sur une liste décroissante. 
                            # Si cette valeur est supérieure ou égale à notre valeur. On met 1 dans matrice2[k1_1][k2_1]
                            if valeur_colonne_1 >= valeur_ligne_1:
                                matrice2[k1_1][k2_1] = 1
                            # Si cette valeur est strictement inférieure à notre valeur. On met -1 dans matrice2[k1_1][k2_1]
                            if valeur_colonne_1 < valeur_ligne_1:
                                matrice2[k1_1][k2_1] = -1

        #print(matrice1)
        #print(matrice2)

        # On calcule le socre total.
        # Calcul du tau:
        # Le numérateur:
        # Somme totale:
        S = 0
        # On a P: le nombre de paires concordantes.
        P = 0
        # On a Q: le nombre de paires non concordantes.
        Q = 0
        # On a que S = P - Q
        # On parcourt les couples:
        # Le but va être de parcourir toutes les paires de possibilités de l'univers.
        # Deux paires sont concordantes si elles ont la même valeur dans matrice1 
        # Que dans matrice2
        # Et pour chacune de ces paires de rajouter plus 1 à P si la paire est concordante
        # Et pour chacune de ces paires de rajouter plus 1 à Q si la paire est non concordante
        # On parcourt tous les indices pour avoir tous les pairs
        for k in range(len(univers)-1): 
            #print("indice k")
            #print(k)  
            for i in range(k+1,len(univers)):
                #print("indice i")
                #print(i)
                # On a matrice1,k,i
                valeur1 = matrice1[k][i]
                # On a matrice2,k,i
                valeur2 = matrice2[k][i]
                #print("valeurs:")
                #print(valeur1)
                #print(valeur2)
                if valeur1 != 0 and valeur2 != 0:
                    #print("les deux différents de 0")
                    if valeur1 == valeur2:
                        P += 1 
                        #print("P")
                        #print(P)
                    if ((valeur1 == 1) and (valeur2 == -1)) or ((valeur1 == -1) and (valeur2 == 1)):
                        Q += 1
                        #print("Q")
                        #print(Q)

        # On a que S = P - Q
        S = P - Q
        #print("P")
        #print(P)
        #print("Q")
        #print(Q)

        # Le dénominateur: Comme dénominateur on prend len(univers)*(len(univers) - 1)/2
        dénominateur = len(univers)*(len(univers) - 1)/2
        #print(dénominateur)
        # Tau
        tau = S/dénominateur
        L_taus.append(tau)
    
    return L_taus

# On résout le problème que dans la première matrice il n'est pas censé avoir des 0.
# Les 0 c'est exclusivement pour les cas où il n'y a pas de valeur. Mais en fait si 
# C'est aussi pour la diagonale.

# Maintenant pourquoi le P ne marche pas. 

"""On va tester avec : [0, 1, 2, 3, 4, 5, 6]
[1, 2, -10, 3, 4, 5, 6]
soit: dictest_3test = {"a":[[0, 1, 2, 3, 4, 5, 6],
[1, 2, -10, 3, 4, 5, 6]]}
un livre de nom "a" et avec comme l1 et l2 nos deux listes. 


#Test
dictest_3test = {"a":[[0, 1, 2, 3, 4, 5, 6],[1, 2, -10, 3, 4, 5, 6]]}
print("tau")
print(fKendall(dictest_3test))"""

# C'est bon ça marche. On a l'exact même résultat que gemini. 
# On peut passer au test sur les fichiers:

# On appelle la fonction: fcréationl.
dictest_3 = fcréationl()
# Et si au contraire il nous manque des fichiers à nous: 
# On aura une liste qui sera plus courte que l'autre.

# Test
#liste_score_kendall = fKendall(dictest_3)
#print("La liste des scores de Kendall est :")
#print(liste_score_kendall)

# On fait la corrélation de Kendall sur tous les livres: 
# On va en donner la moyenne car cela n'a pas de sens de la faire sur tout l'ensemble de livres. 
def score_kendall_total(liste_score_kendall):
    # Nombre de scores:
    n = len(liste_score_kendall)
    # Somme totale des scores:
    S = 0
    for k in range(n):
        S += liste_score_kendall[k]
    # On crée la moyenne
    moyenne_score_kendall = S/n
    return moyenne_score_kendall

# Test
# On lance score_kendall_total(liste_score_kendall)
#tau_kendall_moyen = score_kendall_total(liste_score_kendall)
#print("le tau/score de Kendall moyen est")
#print(tau_kendall_moyen)


""" RESULTATS """
# Les dictionnaires:
dictest1 = fT1()
dictest2 = fT2()
dictest_3 = fcréationl()
# Les résultats
L_rappels, L_précisions, L_fscores, rappel_total, précision_totale, f_score_total = fmétriques(dictest1,dictest2)
liste_score_kendall = fKendall(dictest_3)
tau_kendall_moyen = score_kendall_total(liste_score_kendall)

# On fait les représentations graphiques sous formes d'histogramme:
# Pour les rappels 
plt.bar(list(range(len(L_rappels))),L_rappels)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.xlabel("numéros de livres")
plt.ylabel("rappels")
plt.title("rappels des livres")
plt.show()
plt.hist(L_rappels)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.grid()
plt.xlabel("rappels")
plt.ylabel("Nombre de livres")
plt.title("histogramme des rappels des livres")
plt.show()
print("le rappel total est")
print(rappel_total)
# Pour les précisions
plt.bar(list(range(len(L_précisions))),L_précisions)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.xlabel("numéros de livres")
plt.ylabel("précisions")
plt.title("précisions des livres")
plt.show()
plt.hist(L_précisions)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.grid()
plt.xlabel("précisions")
plt.ylabel("Nombre de livres")
plt.title("histogramme des précisions des livres")
plt.show()
print("la précision totale est")
print(précision_totale)
# Pour les f-score 
plt.bar(list(range(len(L_fscores))),L_fscores)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.xlabel("numéros de livres")
plt.ylabel("f-scores")
plt.title("f-scores des livres")
plt.show()
plt.hist(L_fscores)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.grid()
plt.xlabel("f-scores")
plt.ylabel("Nombre de livres")
plt.title("histogramme des f-scores des livres")
plt.show()
print("le f score total est")
print(f_score_total)

# Les tau de Kendall 
plt.bar(list(range(len(liste_score_kendall))),liste_score_kendall)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xlabel("numéros de livres")
plt.ylabel("taus de kendall")
plt.title("taus de kendall des livres")
plt.show()
plt.hist(liste_score_kendall)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.xlabel("taus de kendall")
plt.ylabel("Nombre de livres")
plt.title("histogramme des taus de kendall des livres")
plt.show()
print("le tau/score de Kendall sans compter les faux positifs moyen est:")
print(tau_kendall_moyen)


# Noter ce que l'on a apprit dans les notes. 
# le taux de Kendall
# Principe mais pas code
# Les représentations graphiques, checker que l'on a bien tout noté. 
# On remplit le canva. Tout depuis le début. 
# Penser à refaire les ajustements, les livres qui sont ratés mais ce n'est pas de ma faute.
# En se servant de ce qu'il y a en dessous: 
# Liste des livres qu'il faut exclure car jeux de données 3 ou voir si des mal foutus que l'on n'a pas détecté:
# Liste des livres où il faut refaire l'annotation et ensuite refaire: 
# Jeu de données que l'on devrait obtenir en sortie
"""
Heading out: marche très bien c’est mon annotation qui est mal faite. indice: 3. 
the wild robot: annotation mal faîte. indice: 12	
the wine makers: annotation mal faîte. indice: 13
the winter of our discontent: annotation mal faîte. indice: 14
three day road: rien ne dit que le premier doit être en premier la toc est mal faite. en fait il est bon. indice: 18
the saints: annotations mal faites en fait il est parfait. indice: 21
The True Love experiment: la toc a été faîte avec la bite. indice: 23
we are legion: annotation mal faîte en fait il est bon. 100%. indice: 28
"""

# Il faut refaire le détecteur de bêtise:
"""
the martian: toc écrite n’importe comment. indice: 7
Twisted Emily: le livre est juste raté. indice: 24
"""
# Si le contenu total du livre est inférieur à une certaine valeur. Plus simplement: On est censé n'avoir que des chapitres et des épilogues et prologues. 
# Donc si un des fichiers a un contenu inféieur à 20 mots c'est qu'il y a un soucis.
# Il faut le faire après le 3.: si dans ceux où l'on a mit 1 après le 3. 
# On fait le canva
# On fait le code
# On test le code: est bon
# On modifie dans le total.py: est bon
# On relance le code.
# On copie colle les graphes dans le powerpoint. Tous les graphes. et les textes qui s'affiche de métriques moyennes.
# Et on récupère aussi les proportions de 1 de -1 et de 0 in fine dans dic3_final et la taille de liste_mauvais_livres.
# On télécharge et envoie le pwp à richard vincent et arthur en expliquant vite fait ce que c'est.
# Refaire le canva. Pour ça et pour: détecteur_de_référence.py

# Refaire les tests sans eux aussi du coup. 

# Quoi faire avec les commentaires en dessous ?

# Mettre le code sur git. 






"""
# On appelle ensuite la fonction:
dictest = fT1()
#print(dictest)"""




















"""PARTIE GRAPHIQUES"""
"""
# Graphe
# On fait deux courbes.
# Une courbe:
# Pour chaque livre: 
# Le % de fichier que l’on a bien retrouvé. 
# Une courbe:
# Pour chaque livre: 
# Le % de fichier qui sont bien à leur places. 

# Il nous faut alors: 
# Ordonnées
# Liste des % de fichier que l’on a bien retrouvé.
L_retrouvésT = []
# Liste des % de fichier qui sont bien à leur places. 
L_bonne_placeT = []
# Absisse:
# Liste des livres: clésT
# On parcourt dictest:
# On récupère toutes ses clés
clésT = list(dictest.keys())
print(clésT)
# On les parcourt:
for cléT in clésT:
    # Pour chaque livre:
    # On parcourt les fichiers, donc ses clés:
    sous_clésT = dictest[cléT].keys()
    # Le nombre de fichiers qui sont bien à leur places
    nb_file_bpT = 0
    # Le nombre de fichiers que l’on a bien retrouvé
    nb_file_brT = 0
    # Le nombre de fichiers en tout.
    nb_fileT = len(sous_clésT)
    # On les parcourt:
    print(sous_clésT)
    for sous_cléT in sous_clésT:
        # On récupère les valeurs:
        [aT,bT] = dictest[cléT][sous_cléT]
        if aT == 1:
            nb_file_brT += 1
            if bT == 1:
                nb_file_bpT += 1
    # On créer les pourcentages:
    # % de fichier que l’on a bien retrouvé. Le rappel.
    pour_centbpT = (nb_file_bpT/nb_fileT)*100
    # % de fichier qui sont bien à leur places. 
    pour_centbrT = (nb_file_brT/nb_fileT)*100
    # On les ajoute aux listes:
    L_retrouvésT.append(pour_centbrT)
    L_bonne_placeT.append(pour_centbpT)

# On les remplace par des chiffres pour que cela soit plus lisible
clésT_2 = [kT_1 for kT_1 in range(len(clésT))]
# On fait le graphe de tout ça:
plt.plot(clésT_2,L_retrouvésT, color="red", label = "rappel")
# plt.plot(clésT_2,L_bonne_placeT, color="blue")
# Pour avoir un axe des ordonnées propre
plt.yticks(np.arange(0, 105, 5))
# Pour nommer l'axe des abscisses:
plt.xlabel("numéros des livres")
# Pour avoir une grille
plt.grid()
plt.show()
"""

"""
# On corrige en enlevant dans les courbes rouge et bleu tous les fichiers
# Et en corrigeant les mauvais. 
# Qui ne correspondant pas aux jeux de données 1. et 2. 
# Ou qui sont juste mal fait. Cf le suivi extraction et traitement
# Pour la courbe bleue: indices qu'il faut mettre égals à la courbe rouge: 
indices_à_égal_rouge = [3,12,13,14,18,21,23,28]
# Pour les courbes rouge et bleu: indices qu'il faut enlever:
# Si on enlève des indices c'est forcément dans les 2:
indices_à_enlever = [1,2,5,7,19,24,25,36,37]
# On s'occupe de rendre les listes égales quand il faut
for kT in range(len(L_bonne_placeT)):
    if kT in indices_à_égal_rouge:
        L_bonne_placeT[kT] = L_retrouvésT[kT]
# On s'occupe de supprimer les indices qu'il faut dans les deux listes. 
L_bonne_placeT = [L_bonne_placeT[kT] for kT in range(len(L_bonne_placeT)) 
                  if kT not in indices_à_enlever]
L_retrouvésT = [L_retrouvésT[kT] for kT in range(len(L_retrouvésT)) 
                  if kT not in indices_à_enlever]
# Et de la liste clésT:
# On les remplace par des chiffres pour que cela soit plus lisible
clésT = [kT for kT in range(len(clésT)) 
                  if kT not in indices_à_enlever]
clésT = [kT_1 for kT_1 in range(len(clésT))]


# On fait le graphe de tout ça:
plt.plot(clésT,L_retrouvésT, color="red")
plt.plot(clésT,L_bonne_placeT, color="blue")
# Pour avoir un axe des ordonnées propre
plt.yticks(np.arange(0, 105, 5))
# Pour avoir une grille
plt.grid()
plt.show()"""