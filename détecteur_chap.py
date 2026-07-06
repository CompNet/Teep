# Partie 4.

"""
Consigne:
les critères de mots que l’on utilise. Il faut les “externaliser”. On crée toutes ces variables dans un autre fichier. Et après on les importe dans le fichier de code.
"""

# les fonctions de détections prennent en variable un texte, le texte du fichier tokénizé sous forme de mots. 
# On a alors une liste python avec dedans les mots. Et le nombre de lignes totale du fichier. Sans les lignes vides ! 
# Du texte. Sous form d'un contenu.
# En sortie on a True si le fichier a été détecté et False sinon. 
# On peut faire en soit tourner autant de fois que l'on veut notre code sur le même dossier d'entrée. Juste cela consomne de la complexité pour rien. 
# Mais le résultat sera toujours le même pour les fichiers. Les dossier de sortie ne sont pas récréés si déjà existants.
# Les fichiers sont remplacés à chaque fois.


# Importations
# Pour la racinisation Stem
from nltk.stem import SnowballStemmer
# On importe critères.py
import critères
# Création de dossiers:
from pathlib import Path
# Création de fichiers:
import os
# Pour la tokenization en mots:
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize


# fonction acknowledgements
def facknowledgements4(L_tokenized4,nb_lignes4):
    # On va raciniser tous les mots du texte
    # On va mettre la liste des racines de références dans critères.py et l'importer: L_racines4
    L_racines4 = critères.L_racines_acknowledgements
    # On choisit le langage à partir duquel on veut raciniser:
    # On le met dans critères.py
    # On l'importe:
    language4 = critères.language
    # On le répercute ici
    stemmer4 = SnowballStemmer(language4)
    # Compteur du nombre de fois où un mot du texte m4 est L_racines4: nbm4
    nbm4 = 0
    # On racinise tous les mots de L_tokenized4:
    for word4 in L_tokenized4:
        # On racinise le mot
        m4 = stemmer4.stem(word4)
        # On va détecter le nombre de fois où un mot du texte m4 est L_racines4: nbm4
        if m4 in L_racines4:
            nbm4 += 1
    # Si le nombre de ligne est nul on retourne False:
    if nb_lignes4 == 0:
        return False
    # On calcule: taille du texte(nombre de lignes)/le nombre de fois où ces mots apparaissent dans le texte = nbm4/nb_lignes4: feature4_1
    feature4_1 = nbm4/nb_lignes4
    # On définit le seuil de 0.3: seuil4
    seuil4 = 0.3
    #On return True si feature4_1 >= seuil4 et False sinon
    if feature4_1 >= seuil4:
        return True
    return False


# Fonction titres de partie ou du livre. ftitles4
def ftitles4(L_tokenized4_1,nb_lignes4_1):
    # Nombre de mots
    n4 = len(L_tokenized4_1)
    # Si moins de 200 mots on enlève: 
    if n4 < 200:
        return True
    # Sinon on return True
    return False


# Fonction copyright 
# Si le texte fait moins de 20 lignes et que le mot copyright ou Copyright 
# Ainsi que le caractère : © apparaisent dedans. 
def fcopyright4(L_tokenized4_2,nb_lignes4_2):
    # On récupère le critère copyright et logo du copyright
    c_Copyright4 = critères.c_Copyright
    logo_Copyright4 = critères.logo_Copyright
    # On regarde si le texte fait moins de 20 lignes:
    if nb_lignes4_2 < 20: 
        # On regarde si on trouve c_copyright4 ou logo_copyright4 dans un des tokens. soit dans L_tokenized4_1
        if (c_Copyright4 or c_Copyright4.lower()) and logo_Copyright4 in L_tokenized4_2:
            return True 
    # Sinon dans tous les cas on return False
    return False


# Fonction glossary
# Elle va prendre celle-ci aussi en variable le texte. 
def fglossary4(L_tokenized4_4,nb_lignes4_4,text4):
    # On détecte le mot "glossary"
    # On récupère le critère glossary
    c_glossary4 = critères.c_glossary
    # On regarde si on trouve c_copyright4 ou logo_copyright4 dans un des tokens. soit dans L_tokenized4_1
    if (c_glossary4 or c_glossary4.lower()) in L_tokenized4_4:
        print("référence à "+c_glossary4)
        return True 
    
    # La densité de ":" par ligne. Plus de 80% 
    # Compteur du nombre de fois où un mot du texte m4 est L_racines4: nbm4
    nbm4_1 = 0
    # On parcourt tous les mots de L_tokenized4:
    for word4_1 in L_tokenized4_4:
        # On va détecter le nombre de fois où un mot du texte word4 est ":":
        if word4_1 == ":":
            nbm4_1 += 1
    # Si le nombre de ligne est nul on retourne True:
    if nb_lignes4_4 == 0:
        print("nombre de lignes nul")
        return True
    
    # On calcule: taille du texte(nombre de lignes)/le nombre de fois où ces mots apparaissent dans le texte = nbm4/nb_lignes4: feature4_1
    feature4_1 = nbm4_1/nb_lignes4_4
    # La densité de ":" par ligne. Plus de 70% 
    seuil4_1 = 0.7
    #On return True si feature4_1 >= seuil4 et False sinon
    if feature4_1 >= seuil4_1:
        print("fort taux de :")
        return True
    
    # Si on détecte une suite de plus 9 lignes où les premiers mots sont dans l'ordre alphabétique.
    # On récupère une liste avec dedans toutes les listes des premières lettres de chaque ligne pour 8 lignes. 
    n4 = 13
    # pourquoi ? Les probas sont de (n parmi 25+n)/(26**n). Avec n le nombre de lignes. 
    # Cf gemini et chatgpt et compréhensible facilement grâce à eux si on veut comprendre. 
    # Soit pour 7 est égal à environ 4*10**(-4)
    # Ca va arrivé environ une fois toutes les 2 000 lignes 
    # Pour 8 c'est 6*10**(-5)
    # Pour 9 c'est 10**(-5).
    # Donc une fois toutes les 10 008 lignes de textes.
    # Pour 13 c'est 2*10**(-9)
    # On peut considérer cette erreur est négligeable. 
    # On récupère une liste avec toutes les premières lettres des lignes dans: text4
    # Sauf les premières lettres des lignes vides. 
    # Liste: Liste_premières_lettre
    Liste_premières_lettre4 = []
    # Pas avec bash. 
    liste_lignes4 = text4.splitlines()
    for ligne4 in liste_lignes4:
        # On vérifie que la ligne existe:
        if ligne4:
            Liste_premières_lettre4.append(ligne4[0])
    Liste_suite4 = []
    for k4 in range(len(Liste_premières_lettre4)-(n4-1)):
        liste_temporaire4 = Liste_premières_lettre4[k4:k4+n4]
        Liste_suite4.append(liste_temporaire4)
    # On parcourt cette liste et on regarde si les lettres y sont dans l'ordre alphabétique. 
    for sous_liste4 in Liste_suite4:
        # On enlève les suites de chiffre:
        # liste des chiffres
        l4 = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Variable garante de pas de chiffres
        a4 = True
        for k in l4:
            if k in sous_liste4:
                # Et donc si on trouve un des chiffres dans sousl_liste4
                # On enlève le garant. 
                a4 = False
        # Si on a un "“" ou "‘" ou "\t" dans la liste:
        # Cela fausse tout. Car on peut se retrouver avec plein deux pour un dialogue. 
        # Cela est toujours dans l'ordre alphabétique vis à vis des lettres.
        # Et surtout ce n'est pas une lettre !!!
        # il faut donc que pas de "“" ou "‘" ou "\t" et que l'on est gardé notre variable garante sur les chiffres. 
        if ("“" not in sous_liste4) and ("‘" not in sous_liste4) and ("\t" not in sous_liste4) and a4 :
            if sous_liste4 == sorted(sous_liste4, reverse=False):
                print("liste de premières lettres dans l'ordre alphabétique : ")
                print(sous_liste4)
                return True 
    
    # Sinon dans tous les cas on return False
    return False


# A propos de l'éditeur:
def fpublisher4(L_tokenized4_5,nb_lignes4_5):
    # On va mettre la liste des racines de références dans critères.py et l'importer: L_racines4
    L_mots_5 = critères.L_mots_publisher
    # racine de publisher
    racine_publisher4 = critères.c_publisher
    # On choisit le langage à partir duquel on veut raciniser:
    # On le met dans critères.py
    # On l'importe:
    language4_5 = critères.language
    # On le répercute ici
    stemmer4_5 = SnowballStemmer(language4_5)
    # Compteur du nombre de fois où un mot du texte m4 est racine_publisher4: nbm4
    nbm4_5 = 0
    # On racinise tous les mots de L_tokenized4_5:
    for word4_5 in L_tokenized4_5:
        # On racinise le mot
        m4_5 = stemmer4_5.stem(word4_5)
        # On va détecter le nombre de fois où un mot du texte m4_5 est racine_publisher4: nbm4_5
        if m4_5 == racine_publisher4:
            nbm4_5 += 1
    # Compteur pour dans L_mots_5
    nbm4_52 = 0
    for word4_52 in L_tokenized4_5:
        # On va détecter le nombre de fois où un mot de la liste L_mots_5 est présent dans un mot. Car ce sont des chose qui sont dans les tokens. 
        for mot_référence5 in L_mots_5:
            if mot_référence5 in word4_52:
                nbm4_52 += 1
    # Compteur pour les chiffres
    nbm4_53 = 0
    for word4_53 in L_tokenized4_5:
        # On racinise le mot
        m4_53 = stemmer4_5.stem(word4_53)
        # On va détecter le nombre de fois où un mot du texte m4_53 est un nombre. 
        # On essaye de transfomer le token en int si on réussit c'est que c'est bon de base on avait un entier?
        try:
            int(m4_53)
            nbm4_53 += 1
        except Exception as e:
            # Dans le cas contraire on fait juste rien du coup.
            nbm4_53 = nbm4_53

    # Si on trouve les données au dessus dans environ 40% des lignes c'est bon. 
    # On fait le nombre final des données au dessus:
    nb_final5 = nbm4_5 + nbm4_52 + nbm4_53
    # Pourquoi 40 ? Au pif. 
    # Si le nombre de ligne est nul on retourne True:
    if nb_lignes4_5 == 0:
        return True
    # On calcule: le nombre de fois où ces mots apparaissent dans le texte/taille du texte(nombre de lignes) = nb_final5/nb_lignes4_5: feature4_5
    feature4_5 = nb_final5/nb_lignes4_5
    # On définit le seuil de 0.4: seuil4_5
    seuil4_5 = 0.4
    #On return True si feature4_5 >= seuil4_5 et False sinon
    if feature4_5 >= seuil4_5:
        return True
    return False


# Fonction Principale:
# On récupère en entrée: dossier_sortie2, dic2, dic3 et L_nom_livres_sansext
def fprincipale5(dict2,dict3,L_nom_livres_sansext):
    # On va parcourir L_nom_livres_sansext
    for nom_livre4 in L_nom_livres_sansext:
        # Pour chaque livre:
        # On va lui créer un dossier dans dossier_sortie4. de nom son nom de livre sans extension toujours. 
        # Définir le chemin du dossier que vous voulez créer
        # Par exemple : "dossier_parent/nouveau_dossier"
        chemin4 = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_sortie4/"+nom_livre4)
        chemin4.mkdir(parents=True, exist_ok=True)
        # On va récupérer son dictionnaire dans dict2: pour d'autres features plus tard. 
        dict_livre4 = dict2[nom_livre4]
        # On va parcourir son dossier dans dossier_sortie2
        # Récupérations : on prend chemin4_1
        chemin4_1 = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_sortie2/"+nom_livre4)
        # On récupère les fichiers:
        liste_fichiers4 = chemin4_1.glob("*")
        print(nom_livre4)
        for fichier4 in liste_fichiers4:
            # Pour chaque fichier on regarde si il a déjà été traité à l'aide de dict3 
            # On récupère son nom sans extension
            nom_seul4 = fichier4.stem
            print("pour le fichier "+nom_seul4)
            # On récupère sa valeur dans dict3: dict3[nom_livre4][nom_seul4]
            valeur4 = dict3[nom_livre4][int(nom_seul4)]
            # On va alors utiliser dict2 
            # Variables qu'il faut: L_tokenized4,nb_lignes4, text4, soit respectivement le texte du fichier tokenizé, son nombre de ligne, le texte
            # On récupère donc le texte du fichier
            with open(fichier4, "r", encoding="utf-8") as f4:
                contenu4 = f4.read()
            # Si dans dict3 on trouve 0:
            if valeur4 == 0:
                # Puis son nombre de lignes. Sans les lignes vides 
                # La liste des lignes 
                ligne_texte4 = contenu4.splitlines()
                # On récupère le nombre de lignes non vides
                nb_lignes_texte_sansvides4 = 0
                for ligne4 in ligne_texte4:
                    if (ligne4 != "") and (ligne4 != " "):
                        nb_lignes_texte_sansvides4 +=1
                # Puis on le tokenize en mots
                tokenized_contenu4 = word_tokenize(contenu4)
                # On va appeler les différentes méthodes de détections
                # Compteur de True
                compteur4 = 0
                # facknowledgements4(L_tokenized4,nb_lignes4)
                if facknowledgements4(tokenized_contenu4,nb_lignes_texte_sansvides4):
                    compteur4 += 1
                    print("detect facknowledgements4")
                # ftitles4(L_tokenized4_1,nb_lignes4_1)
                if ftitles4(tokenized_contenu4,nb_lignes_texte_sansvides4):
                    compteur4 += 1
                    print("detect ftitles4")
                # fcopyright4(L_tokenized4_2,nb_lignes4_2)
                if fcopyright4(tokenized_contenu4,nb_lignes_texte_sansvides4):
                    compteur4 += 1
                    print("detect fcopyright4")
                # fglossary4(L_tokenized4_4,nb_lignes4_4,text4)
                if fglossary4(tokenized_contenu4,nb_lignes_texte_sansvides4,contenu4):
                    compteur4 += 1
                    print("detect fglossary4")
                # fpublisher4(L_tokenized4_5,nb_lignes4_5)
                if fpublisher4(tokenized_contenu4,nb_lignes_texte_sansvides4):
                    compteur4 += 1
                    print("detect fpublisher4")
                # Si elles retournent True. Soit compteur4 >= 1: Alors on met -1 dans dict3 
                if compteur4 >= 1:
                    dict3[nom_livre4][int(nom_seul4)] = -1
            # On prend la valeur de dict3 et si elle est de 0 ou 1 on met notre fichier alors dans dossier_sortie4 dans le sous dossier de son livre. 
            # dans dossier: chemin4 à reprendre:
            # Fichier de nom : même nom: mais avec l'extension texte bien sûr. soit: fichier4.name
            # Et dedans on met contenu4
            if (dict3[nom_livre4][int(nom_seul4)] == 0) or (dict3[nom_livre4][int(nom_seul4)] == 1):
                chemin_complet4 = os.path.join(chemin4, fichier4.name)
                with open(chemin_complet4, 'w', encoding='utf-8') as f4_1: 
                    f4_1.write(contenu4) 
                
    return dict3



