# 3. 
# Fonction qui va créer notre dictionnaire:

"""On arrive ensuite dans le détecteur de référence à chapitre, prologue, épilogue. On utilise A. et B.b. 
le texte d’entrée A. et le  nom du fichier B.b.
Pour les 1. 88%: livres aux entrées identifiées, on en récupère les fichiers qui comptent
Avec un détecteur simple de:
Pas de détecteur de cha. On peut avoir des titres de livres avec ça dedans. Trop large. 
On fait un truc simple il faut détecter chapter sous toutes ses formes. 
Voir pour épilogue et prologue. De même.
les critères de mots que l’on utilise. Il faut les “externaliser”. 
On crée toutes ces variables dans un autre fichier: critères.py 
Et après on les importe dans le fichier de code.

Sinon, aussi avant:
pour une approche avec le .ncx:
On peut récupérer tous ceux dont le texte est juste un chiffre de 1 ou 2 caractères ou/et au niveau livre 
quand mit bout à bout ils forment une suite de chiffres dans le .ncx. 
On va considérer qu'il ne peut y avoir normalement qu'une seule suite de nombres par toc. Donc que l'on n'a 
à détecter qu'une seule suite de nombres. 

Pour la fonction globale:
On a en entrée: dictionnaire1: Comme clé on prend le titre originel du livre. et: L_nom_livres_sansext. La liste des noms des livres sans extension. 
Le titre de son dossier epub. Sans extension bien sur. 
Livres qui ont comme valeur une liste. Où on met successivement A. et B.b. pour chaque fichier. 
le texte d’entrée A. et le  nom du fichier B.b.
Un fichier a alors ses A. et B.b pour l’indice de la liste: son nom-1.

On veut en sortie: pour chaque livre si détecté comme chapitre: dic3:
dictionnaire: nom livre: puis dedans dictionnaire selon le nom du fichier: et la valeur 0 ou 1 si c'est un chapitre ou non.
"""


# On va créer des fonctions à chaque fois pour chaque détection: 

# Une fonction pour la détection pour les termes A et B.b. un par un: f1détec3
# Notre fonction est donc une fonction qui va prendre en entrée: le texte d’entrée A. et le nom du fichier B.b.
# Et elle va retourner True si on a detecté pour A ou B une référence au mots: chapitre, prologue et épilogue
# Et False sinon.
# Les if que l'on va étudier sont:
# En prenant exemple sur la langue anglaise:
# If on trouve chapter, epilogue, prologue dans le nom. 
# On prend alors le texte et on le met en minuscule et on voit 
# Si on détecte chapter, epilogue, prologue. 
# Il faut alors mettre ce qu'il y a besoin dans critères 
# Et les importer:
import critères
c_chapter3 = critères.c_chapter
c_prologue3 = critères.c_prologue
c_epilogue3 = critères.c_epilogue
# On met aussi ces critères: 
"""
copyright
epigraph 
glossary
about the author
aubout the publisher
also by
"""
c_copyright3 = critères.c_copyright
c_epigraph3 = critères.c_epigraph 
c_glossaryr3 = critères.c_glossary
c_about_author3 = critères.c_about_author 
c_about_publisher3 = critères.c_about_publisher
c_also_by3 = critères.c_also_by
# Et dans ce cas là il faut mettre -1. 
# On remplit les if dans le code:
def f1détec3(A,Bb):
    # On va créer une liste avec dedans A et Bb
    L_3 = [A,Bb]
    # On va parcourir cette liste
    for text3 in L_3:
        # On va récupérer text et le mettre en minuscule:
        Text3 = text3.lower()
        # On fait un if par critère
        #On fait les cas -1 avant car ils exclue les suivant
        if c_copyright3 in Text3:
            return -1
        if c_epigraph3 in Text3:
            return -1
        if c_glossaryr3 in Text3:
            return -1
        if c_about_author3 in Text3:
            return -1
        if c_about_publisher3 in Text3:
            return -1
        if c_also_by3 in Text3:
            return -1
        # Avec: if .. in : return True
        if c_chapter3 in Text3:
            return True
        if c_prologue3 in Text3:
            return True
        if c_epilogue3 in Text3:
            return True
    # Après avoir parcouru toute la liste et n'avoir pas return un True. 
    # On return alors un False
    return False

# Un fonction pour la détection de chapitres en fonction de tout le livre. 
# Algo pour python: 
# la fonction: f2détec3
# On récupère en entrée la liste pour chaque livre.
# Liste de sous liste de A. et B/b pour chaque fichier
def f2détec3(L_livre3):
    # Variables à créer
    # On crée deux listes:
    # Une: les premiers éléments de chaque sous liste. LL3
    LL3 = [k13 for [k13,k23] in L_livre3]
    # Une deuxième: les deuxièmes éléments de chaque sous liste. LLL3
    LLL3 = [k23 for [k13,k23] in L_livre3]
    # On les mets dans ML3.
    ML3 = [LL3,LLL3]
    # Lj3: la liste des indices j3 si ils sont des chapitres ou non. 0 ou 1. 
    # Pour l'instant 0 et de taille len(L_livre3)
    Lj3 = [0 for k3 in L_livre3]
    # Code en lui même:
    # On parcourt ML3. On prend ml3
    for ml3 in ML3:
        # a3: si la fois d'avant on a détecté un 1. De valeur True ou False.
        a3 = False
        # b3: si on est sur la bonne voie. De valeur True ou False.
        b3 = False
        # c3: valeur chiffrée précédente du texte
        c3 = 0
        # jj3: valeur de l'indice pour lequel on trouve 1 et qu'il faut garder en mémoire. 
        jj3 = 0
        # On parcourt ml3. j3
        for j3 in range(len(ml3)):
            # On regarde si b3 est True
            if b3 == True:
                # Dans ce cas là on regarde juste si le texte (ml3[j3]) est bien le nombre suivant. bien c3 + 1. 
                if ml3[j3] == str(c3):
                    # Et on fait c3+=1
                    c3+=1
                    # On garde aussi l'indice du texte. j3. Dans Lj3. On le met à 1.
                    Lj3[j3] = 1
            # Sinon: on regarde si a3 est True
            elif a3 == True:
                # on regarde au rang si on a 2.
                if ml3[j3] == "2":
                    # Si oui c'est que donc on est sur une bonne lancée. 
                    # On met alors c3 = 3. 
                    c3 = 3
                    # et b3 = True
                    b3 = True
                    # On garde aussi l'indice du texte. j3. Dans Lj3. On le met à 1.
                    Lj3[j3] = 1
                    # On garde aussi l'indice du texte précédent. Maintenant on sait qu'il est bon.
                    # jj3. Dans Lj3. On le met à 1.
                    Lj3[jj3] = 1
                #et si pas 2 on remet a3 à False.
                else:
                    a3 = False
            # Sinon: on fais le test pour savoir si il y a un 1. 
            else:
                # Si l'on détecte le chiffre 1 tout seul. 
                if ml3[j3] == "1":
                    # On met True à a3 
                    a3 = True
                    # On met cet indice: j3 dans jj3 pour le garder en mémoire en attendant le 2.
                    jj3 = j3
    # A la fin, en sortie: on a donc Lj3 où on a des 1 pour tous les indices des fichiers qui sont des chapitres. 
    return Lj3


# fonction finale qui va les appeler:
def fabrication_dictionnaire3(dict,L_nom_livres_sansext3):
    #On va créer le dictionnaire final: dic_3
    dic_3 = {}
    # On va parcourir L_nom_livres_sansext3
    for nom_livre3 in L_nom_livres_sansext3:
        # On crée un dictionnaire pour le livre dans dic_3:
        dic_3[nom_livre3] = {}
        # Et pour chaque livre aller chercher sa valeur dans dict
        L_3 = dict[nom_livre3]
        # Sa valeur qui est donc: comme valeur une liste. L_3. Où a successivement A. et B.b. pour chaque fichier. 
        # L_3 = [[A.,B.b.],..,[A.,B.b.]]
        # Le texte d’entrée A. et le  nom du fichier B.b.

        # On passe alors L_3 dans f2détec3(L_livre3)
        L_result3 = f2détec3(L_3)
        
        # On parcourt ensuite L_3 pour f1détec3([A.,B.b.])
        for kk3 in range(len(L_3)):
            # L_3[kk3] = [A.,B.b.]
            # On a que cela correspond au fichier de nom: Un fichier a alors ses A. et B.b pour l’indice de la liste: son nom-1 i.e. indice de la liste + 1 : son nom
            #Ainsi: nom_fichier3 = kk3 + 1
            nom_fichier3 = kk3 + 1
            # Et pour chaque sous liste, on la passe dans: f1détec3(L_3[kk3]) = f1détec3([A.,B.b.])
            valeur_3 = f1détec3(L_3[kk3][0],L_3[kk3][1])
            # On en applique les conséquences
            # Si True c'est que l'on a trouvé au moins une référence à chapter, prologue.. dans ce fichier
            # Ou que L_result3[kk3] == 1
            # Donc pour l'instance du sous dictionnaire du livre pour le fichier on met 1
             #Pour le cas où on sait que ce n'est pas un chapitre par f1détec3
            if valeur_3 == -1:
                dic_3[nom_livre3][nom_fichier3] = -1
            elif valeur_3 == True or L_result3[kk3] == 1:
                dic_3[nom_livre3][nom_fichier3] = 1
            # Et sinon on met 0
            else:
                dic_3[nom_livre3][nom_fichier3] = 0
        
        print(nom_livre3)
    
    return dic_3

