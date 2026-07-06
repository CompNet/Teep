# Test: Fichier de test pour tester
# T à la fin des variables

# Importations
# Pour la gestion de fichiers et de dossiers:
import os
from pathlib import Path 
# Tri naturel
from natsort import natsorted
# Pour le graphique
import matplotlib.pyplot as plt
import numpy as np

# Fonction fT
def fT():
    # On remet dictest à {}
    dictest = {}
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
    # On parcourt les dossiers du dossier annoté. 
    for k in range(len(sous_dossiers_pathT)):
        # Pour chaque dossier:
        # On crée sa clé dans dictest et le sous dictionnaire associé. 
        # On récupère le nom du sous dossier
        nameT = sous_dossiers_nameT[k]
        # On dit qu'on y est:
        print(nameT)
        # On créer sa clé:
        dictest[nameT] = {}
        # On crée l'indice de position du fichier initial. Initialisé à 0.
        id_positionT = 0
        # On le parcourt. On en récupère tous les fichiers du dossier:
        # On récupère le path du dossier:
        dossier_atuelT = sous_dossiers_pathT[k]
        # On en récupère tous les fichiers textes
        # On en a une liste: 
        fichiersT = os.listdir(dossier_atuelT)
        # On range cette liste dans l'ordre croissant: 
        fichiersT = natsorted(fichiersT)
        # On la parcourt:
        for fichierT in fichiersT: 
            # On ajoute +1 à l'indice de position du fichier initial
            id_positionT += 1
            # C'est l'indice courant de notre fichier. 
            pas_vrai = id_positionT
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
            # On range cette liste dans l'ordre croissant: 
            # On sait que ce sont forcément des entiers. Car c'est nous qui avons renommer nos fichiers ainsi.
            # Donc cela donnera le code suivant: 
            fichiers_non_annotéT = sorted(fichiers_non_annotéT, key=int)
            # on initialise les pas: à 1
            pasT = 0
            # On initialise aT et bT à 0:
            aT = 0
            bT = 0
            # On va essayer de voir si on le retrouve bien dans le dossier des résultats 
            # Et si il est à la même place. 
            # Parcourir les fichiers dans l'ordre croissant. 
            for fichier_non_annotéT in fichiers_non_annotéT:
                # On compte les pas 
                # On ajoute 1 
                pasT += 1
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
                    # On note le pas où on se trouve
                    pas_résultat = pasT
            # si on a trouvé le fichier on regarde si le pas correspond bien à l'indice
            if aT == 1:
                if pas_vrai == pas_résultat:
                    bT = 1
            # On en crée la liste 
            liste_fichierT = [aT,bT]
            # On met la liste dans dictest
            # On récupère le nom du fichier avec extension parce que l'on s'en fiche avec ou sans: 
            name_fileT = fichierT
            dictest[nameT][name_fileT] = liste_fichierT
    
    return dictest
 
# On appelle ensuite la fonction:
dictest = fT()
#print(dictest)

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
    # % de fichier que l’on a bien retrouvé.
    pour_centbpT = (nb_file_bpT/nb_fileT)*100
    # % de fichier qui sont bien à leur places. 
    pour_centbrT = (nb_file_brT/nb_fileT)*100
    # On les ajoute aux listes:
    L_retrouvésT.append(pour_centbrT)
    L_bonne_placeT.append(pour_centbpT)

# On les remplace par des chiffres pour que cela soit plus lisible
clésT_2 = [kT_1 for kT_1 in range(len(clésT))]
# On fait le graphe de tout ça:
plt.plot(clésT_2,L_retrouvésT, color="red")
plt.plot(clésT_2,L_bonne_placeT, color="blue")
# Pour avoir un axe des ordonnées propre
plt.yticks(np.arange(0, 105, 5))
# Pour avoir une grille
plt.grid()
plt.show()


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
plt.show()