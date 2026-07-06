#1. Récupération des données: 
#a. On trouve le .ncx. 
#faire une fonction avec le code: f1
#On va faire une fonction avec notre code.
# Elle va prendre, en entrée: le dossier d'entrée dans: dossier1a
# Elle va prendre, en sortie: nos deux dictionnaires avec nos données et bien sur elle rempli aussi le dossier de sortie: dossier_sortie1.
# On peut faire en soit tourner autant de fois que l'on veut notre code sur le même dossier d'entrée. Juste cela consomne de la complexité pour rien. 
# Mais le résultat sera toujours le même pour les fichiers. Les dossier de sortie ne sont pas récréés si déjà existants.
# Les fichiers sont remplacés à chaque fois.

#importations
#pour l'ouvertue du dossier epub
from pathlib import Path
#gestion de epubs
from ebooklib import epub
#parcourt de code xml/xhtml
from bs4 import BeautifulSoup 
#importation pour la création de fichiers
import os
#importations
import zipfile

# fonction de récupération du nom à partir du chemin sans / et #
def detectsalahhashtag(nom1):
    #On va récupérer l'indice du dernier "#": l1b_1
    #On l'initialise à -1 si rien n'arrive on ne le bouge pas de cette manière. 
    l1b_1 = -1
    #En parcourant la chaîne de caractère nom1.
    for ll1b_1 in range(len(nom1)):
        if nom1[ll1b_1] == "#":
            l1b_1 = ll1b_1
    #On récupère ensuite le nom du fichier si on a trouvé un "#"
    if l1b_1 != -1:
    #chemin_fichier1b[:l1b] Afin du coup d'éviter le "#" en l1b. 
        way1b_1 = nom1[:l1b_1]
    #Sinon on garde le nom du chemin. C'est que le chemin est le nom du fichier. 
    else:
        way1b_1 = nom1
    #On récupère le nom du fichier
    #il faut récupérer la dernière composante du chemin après le dernier "/"
    #On récupère le fichier et on l'ouvre. On a donc le chemin du fichier dans le livre qui est chemin_fichier1b.
    #On va juste récupérer le dernier texte après le dernier: "/" et on a le nom du fichier avec bien son extension. 
    #On va récupérer l'indice du dernier "/": j1b
    #On l'initialise à -1 si rien n'arrive on ne le bouge pas de cette manière. 
    j1b = -1
    #En parcourant la chaîne de caractère chemin_fichier1b.
    for kk1b in range(len(way1b_1)):
        if way1b_1[kk1b] == "/":
            j1b = kk1b
    #On récupère ensuite le nom du fichier si on a trouvé un "/"
    if j1b != -1:
    #way1b_1[j1b+1:] Afin du coup d'éviter le "/" en j1b. 
        nom_fichier1b = way1b_1[j1b+1:]
    #Sinon on garde le nom du chemin. C'est que le chemin est le nom du fichier. 
    else:
        nom_fichier1b = way1b_1
    return nom_fichier1b


# Fonction de de voir si on est sur un .ncx ou sur un nav.xhtml: fncxornav
def fncxornav(content1,nom_complet1):
 #variable pour dire si on a trouvé un ncx:
    ncx = 0

    #voir si il n'y a pas un .ncx dedans
    try: 
        #On sait faire normalement
        #On récupère l'id du ncx:
        #Utilisation du parseur xml de BeautifulSoup
        soup = BeautifulSoup(content1, "xml")
        #On va récupérer dans le spine l'attribut de la classe "toc", dans att1a
        #si on veut juste la balise d’un certain nom: 'spine' ici
        BAlise1a = soup.select_one('spine')
        #On va récupérer dans le spine l'attribut de la classe "toc", dans att1a
        att1a = BAlise1a.get("toc")
        #Pas de soucis de trouver ici un nav.xhtml dans le spine. Cela voudrait dire que l'on suit la norme epub3 or dans celle-ci on a abandonné le spine. 
        #Si on le trouve pas c'est que c'est alors "ncx", dans att1a
        if att1a == None:
            att1a = "ncx"
        #0n récupère la balise qui possède pour sa classe id l'attribut att1a
        # 1. On cherche la balise qui a id = att1a
        # Syntaxe CSS : balise[attribut='valeur']
        balise1a = soup.select_one('[id ='+ att1a + ']')
        #Dans cette balise on va alors récupérer la valeur de l'attribut pour la classe href
        #On aura alors le chemin du fichier .ncx
        cheminncx1a = balise1a.get("href")
        ncx = 1
        #On dit que l'on a trouvé le fichier .ncx pour ce livre 
        print("a .ncx for the book:"+nom_complet1) 
                
    except Exception as e:
        #On dit que l'on n'a pas trouvé de fichier .ncx pour ce livre 
        print("no .ncx for the book:"+nom_complet1)

    #voir si il n'y a pas de nav.xhtml
    #comment faire ? 
    #pour regarder si il n'y a pas un nav.xhtml. 
    #On regarde si une classe id n'a pas pour attribut: "toc"
    try: 
        #On sait faire normalement
        #On récupère l'id du nav:
        #Utilisation du parseur xml de BeautifulSoup
        soup = BeautifulSoup(content1, "xml")
        #0n récupère la balise qui possède pour sa classe id l'attribut "toc"
        try:
            # 1. On cherche la balise qui a id = "toc"
            # Syntaxe CSS : balise[attribut='valeur']
            balise1a = soup.select_one('[id = "toc"]')
            #Dans cette balise on va alors récupérer la valeur de l'attribut pour la classe href
            #On aura alors le chemin du fichier nav.xhtml
            cheminnav1a = balise1a.get("href")
            #On dit que l'on a trouvé un fichier nav autre que le .ncx pour ce livre 
            print("a nav.xhtml for the book:"+nom_complet1) 
        # Sinon: on essaye:
        # 0n récupère la balise qui possède pour sa classe id l'attribut "nav"
        except:
            try:
                # 1. On cherche la balise qui a id = "nav"
                # Syntaxe CSS : balise[attribut='valeur']
                balise1a = soup.select_one('[id = "nav"]')
                #Dans cette balise on va alors récupérer la valeur de l'attribut pour la classe href
                #On aura alors le chemin du fichier nav.xhtml
                cheminnav1a = balise1a.get("href")
                #On dit que l'on a trouvé un fichier nav autre que le .ncx pour ce livre 
                print("a nav.xhtml for the book:"+nom_complet1) 
            except Exception as e:
                #On dit que l'on n'a pas trouvé de fichier nav autre que le .ncx pour ce livre 
                print("pas de nav avec id: nav") 
            
        #Attention parfois l'attribut toc peut être donné pour le .ncx. Donc dans ce cas là on l'a trouvé dans le spin et donc plus haut. 
        #c'est pour ça que après on fait que si on a trouver quelque chose pour .ncx on s'arrête là dessus

    except Exception as e:
        #On dit que l'on n'a pas trouvé de fichier nav autre que le .ncx pour ce livre 
        print("no nav.xhtml for the book:"+nom_complet1) 
    
    #si on a trouvé un .ncx et un fichier nav.xhtml ou autre on renvoit le chemin du .ncx:
    #ou si on a que .ncx 
    if ncx == 1:
        cheminfinal1a = cheminncx1a
    #si on n'a pas le .ncx c'est l'autre le chemin final
    else:
        cheminfinal1a = cheminnav1a

    # On a aussi besoin du ncx:
    return cheminfinal1a, ncx



# fonction de récupération du nom à partir du chemin sans #
def detecthashtag(nom1_1):
    #On va récupérer l'indice du dernier "#": l1b_1
    #On l'initialise à -1 si rien n'arrive on ne le bouge pas de cette manière. 
    l1b_2 = -1
    #En parcourant la chaîne de caractère nom1.
    for ll1b_2 in range(len(nom1_1)):
        if nom1_1[ll1b_2] == "#":
            l1b_2 = ll1b_2
    #On récupère ensuite le nom du fichier si on a trouvé un "#"
    if l1b_2 != -1:
    #chemin_fichier1b[:l1b] Afin du coup d'éviter le "#" en l1b. 
        way1b_2 = nom1_1[:l1b_2]
    #Sinon on garde le nom du chemin. C'est que le chemin est le nom du fichier. 
    else:
        way1b_2 = nom1_1
    return way1b_2


def f1(nom_dossier_entrée):
    #liste des mauvais livres
    L_mauvais_livres = []
    #On crée les dictionnaires:
    dic1 = {}
    dic2 = {}
    #Liste avec le nom des fichiers sans extensions
    L_fichiers1a = []
    #il faut ouvrir tous les dossiers epubs
    #on sait faire normalement
    #On sélectionne le dossier où trouver les fichiers 
    #on récupère le dossier:
    #Récupérations 
    #le dossier 
    dossier1a = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+ nom_dossier_entrée)
    #On ouvre ce dossier 
    #On parcourt les fichiers dedans
    #on récupère les fichiers:
    #Pour être sur de sur on ne récupère que les fichiers epub
    liste_fichiers1a = dossier1a.glob("*.epub")
    #On parcourt les fichiers epubs:
    for fichier1a in liste_fichiers1a:
        
        #On récupère le nom complet du fichier, avec extension
        nom_complet1a = fichier1a.name
        #Nom complet du livre sans extension
        nom_sansext1a = fichier1a.stem
        #Pour chaque fichier dedans on l'ouvre.
        #On essaye de l'ouvrir et si c'est un mauvais on le met dans la liste des mauvais:

        try: 
            book1a = epub.read_epub(fichier1a)

            #On ne crée logiquement pas de dossier pour les mauvais livres donc on crée le dossier seulement ici:
            #On crée un dossier avec ce nom dans: dossier_sortie1
            #On crée son chemin
            chemindossier1a = Path("dossier_sortie1/"+nom_sansext1a)
            # Créer le dossier
            # parents=True : crée aussi les dossiers parents s'ils n'existent pas
            # exist_ok=True : ne renvoie pas d'erreur si le dossier existe déjà
            chemindossier1a.mkdir(parents=True, exist_ok=True)
            #On ajoute le Nom complet du livre sans extension: nom_sansext1a à la Liste avec le nom des fichiers sans extensions: L_fichiers1a
            L_fichiers1a.append(nom_sansext1a)

            #On récupère le opf
            #On trouve le chemin du .opf en passant par le container:

            #On récupère le contenu du container

            #On créer un outil qui permet de parcourir le fichier zip:
            #ici en mode lecteur
            with zipfile.ZipFile(fichier1a, 'r') as z:
                #On a que ce chemin est bien le même pour tous les container.xml.
                container = z.read('META-INF/container.xml')

            #On parcours le container avec beautifulsoup et on en récupère le chemin du .opf:
            #On a que le chemin vers celui-ci est toujours au même endroit.
            #Il faut aller dans la balise "rootfile" et récupérer l’attribut de la classe: "full-path"

            #On se met dans la balise "rootfile"

            #initialisation du parseur xml par exemple:
            #pour un html et xhtml:”lxml”.
            #le container.xml c’est logiquement du xml
            soup1a = BeautifulSoup(container, "xml")

            #si on veut juste la balises d’un certain nom:
            Balise1a = soup1a.select_one("rootfile")

            #On récupère l’attribut de la classe: "full-path"
            chemin1a = Balise1a.get("full-path")

            #On ouvre ensuite le .opf et on récupère son contenu grâce à son chemin: 

            #On créer un outil qui permet de parcourir le fichier zip:
            #ici en mode lecteur
            with zipfile.ZipFile(fichier1a, 'r') as z:
                #On peut trouver et lire ici un fichier à partir de son chemin dans le dossier.
                #on met son contenu dans content1a
                content1a = z.read(chemin1a)

            # Le chemin à utiliser 
            cheminfinal1a, ncx = fncxornav(content1a,nom_complet1a)

            #On est passé au 1.b.

            #Nom complet du livre sans extension:
            nom_sansext1b = fichier1a.stem 

            #On crée la clé du livre dans dic1 et dans dic2
            #avec le nom du livre dans le dossier sans extension: 
            dic1[nom_sansext1b] = []
            dic2[nom_sansext1b] = {}
            
            #On récupère le fichier et on l'ouvre. On a donc le chemin du fichier dans le livre qui est cheminfinal1a.
            #On va juste récupérer le dernier texte après le dernier: "/" et on a le nom du fichier avec bien son extension. 
            nomtoc1b = detectsalahhashtag(cheminfinal1a)

            #On ouvre le fichier:

            #On reparcourt le livre où l'on est à la recherche du fichier avec ce nom:
            #Ici on ne va jamais modifier le contenu de la toc onn veut juste extraire des choses de son contenu. 
            #Dans le livre: book1a
            for item1b in book1a.get_items():
                # On enlève les / dans le nom: Au cas où la toc est dans un dossier et pas à la racine de l'epub. 
                nom_item1b = detectsalahhashtag(item1b.get_name())
                if nom_item1b == nomtoc1b:
                    #on en récupère le contenu.
                    content1b = item1b.get_content()
            
            #On va faire maintenant deux cas en fonction que le fichier toc ouvert soit un .ncx ou un nav.xhtml 
            #si c'est .ncx 
            if ncx == 1:
                
                #on récupère chaque fichier avec beautifulsoup: 
                #Il faut récupérer toutes les balises navPoint: 
                #initialisation du parseur xml pour .ncx:
                #sur content1b
                soup = BeautifulSoup(content1b, "xml")
                # On récupère toutes  les balises correspondantes aux critères sous forme d’une liste python classique:
                balises1b = soup.select('navPoint') 
                #On a le compte total des fichiers: c1b 
                #c1b c'est la taille de la liste balises1b
                #Car on a autant de navPoint que de fichiers. 
                c1b = len(balises1b)
                #il faut donc dans le cas .ncx si on trouve None pour le playorder on passe sur une structure comme en nav.xhmtl où on compte nous même pour faire le playorder.
                #Ou plutôt on compte dans tous les cas et si le playorder est None on met la valeur que l'on a comptée nous. 
                #On initialise le playOrder à 1. 
                myPlayOrder1b = 1
                # On peut alors les parcourir comme n’importe quelle liste python.
                #b1b c'est la balise navPoint en cours.
                for b1b in balises1b:
                    #Pour chaque fichier: 
                    #On récupère le playorder: On ne le récupère plus des fois il est calamiteux. 
                    #pour le playorder de secours il va falloir le faire nous même. 
                    Current_playorder = myPlayOrder1b
                    #On lui ajoute 1 pour le fichier suivant
                    myPlayOrder1b += 1
                    #On prend le chemin du fichier:
                    #Il est dans la sous balise : content 
                    #On trouve la sous balise content
                    balise_content1b = b1b.find('content')
                    #On y trouve l'attribut de la classe src. 
                    chemin_fichier1b = balise_content1b.get("src")
                    #Il faut enlever la partie après le # si elle existe.
                    #Mais seulement le # pas le /
                    nom_fichier1b = detecthashtag(chemin_fichier1b)

                    #On parcourt le dossier du livre à la recherche d'un fichier avec ce nom
                    #Dans le livre: book1a
                    for item1b in book1a.get_items():
                        if item1b.get_name() == nom_fichier1b:
                            #on en récupère le contenu.
                            content_1b = item1b.get_content()
                    
                    #On va dans le dossier de sortie: "dossier_sortie1/"+nom_sansext1b
                    #On crée un fichier de nom le playorder: playorder1b
                    #chemin du dossier pas en path forcément. 
                    dossier1b = "dossier_sortie1/"+nom_sansext1b
                    # Nom du fichier
                    # On considère que l'on va prendre tout le temps le palyorder que l'on a fait nous même. 
                    nom_fichier_final1b = str(Current_playorder)
                    chemin_complet1b = os.path.join(dossier1b, nom_fichier_final1b) 
                    # Le mode 'w' (write) crée le fichier s'il n'existe pas ou l'écrase s'il existe. 
                    with open(chemin_complet1b, 'wb') as f1b: 
                        #On met le contenu dedans: le contenu: content_1b
                        f1b.write(content_1b) 
                    #Et c'est bon
                    #On rajoute à dic1 les infos sur ce fichier. le texte d’entrée A. et le nom du fichier B.b.
                    #On récupère A.
                    #il faut aller dans la balise fille de b1b, aller dans la balise navLabel
                    balise_navLabel1b = b1b.navLabel
                    #puis aller elle même dans sa fille: "text"
                    balise_text1b = balise_navLabel1b.find("text")
                    #On peut alors récupérer la valeur du contenu de celle-ci
                    A1b = balise_text1b.get_text()
                    #On récupère B.b.
                    Bb1b = nom_fichier1b
                    #On les met dans une liste et on ajoute cette liste dans le dictionnaire dic1. 
                    # Il faut aller voir la clé: nom du titre  du livre sans extension: nom_sansext1b
                    #On ajoute alors à la valeur associée à cette clé: .append([A.,B.b.])
                    dic1[nom_sansext1b].append([A1b,Bb1b])
                    #On remplit dic2. 
                    #Comme clé on a le titre originel du livre. Le titre de son dossier epub.  
                    #Sans extension bien sur: nom_sansext1b
                    #Pour chaque clé livre on a alors un dictionnaire avec comme clés: les fichiers. 
                    #Les clés se sont leurs titres, donc les navpoint. Et les valeurs sous forme de liste:
                    dic2[nom_sansext1b][Current_playorder]=[c1b,Bb1b,Current_playorder]

            #si c'est nav.xhmtl. Soit else:
            else: 
                #On en a le content: content1b
                #On repère chaque fichier avec beautifulsoup: 
                #On créer un paseur pour xhtml.
                #initialisation du parseur en xml:”xml”.
                soup = BeautifulSoup(content1b, "xml")
                #On va dans la première balise ol. On veut juste la première. 
                #si on veut juste la balises d’un certain nom: ol
                balise1b = soup.select_one('ol')
                #On en récupère toutes les balises li.
                sous_balises1b = balise1b.find_all("li")
                #On a le compte total des fichiers: cc1b 
                #cc1b c'est la taille de la liste sous_balises1b
                #Car on a autant de navPoint que de fichiers. 
                cc1b = len(sous_balises1b)
                # On peut alors les parcourir comme n’importe quelle liste python.
                #sous_balise1b c'est la balise navPoint en cours.
                #On initialise le playOrder à 1
                MyPlayOrder1b = 1
                #On parcourt alors toutes ces balises:
                for sous_balise1b in sous_balises1b:
                    #On va s'aider du travail fait sur le .ncx pour tout sauf beautifulsoup.
                    #il faut alors dans tous les cas aller dans la balise fille: 
                    sous_sous_balise1b = sous_balise1b.a
                    #On en récupère: 
                    #Pour chaque fichier: 
                    #On récupère le playorder:
                    #pour la nav pas de playorder il va falloir le faire nous même. 
                    current_playorder = MyPlayOrder1b
                    #On lui ajoute 1 pour le fichier suivant
                    MyPlayOrder1b += 1
                    #On prend le chemin du fichier:
                    #Il nous faut l'attribut de la classe href. 
                    chemin1b = sous_sous_balise1b.get("href")
                    #Il faut enlever la partie après le # si elle existe. Et les / dans le nom: car on a des soucis de / et d'où partent les chemins. 
                    nom_file1b = detectsalahhashtag(chemin1b)

                    #On parcourt le dossier du livre à la recherche d'un fichier avec ce nom
                    #Dans le livre: book1a
                    for Item1b in book1a.get_items():
                        # On enlève les / dans le nom: car on a des soucis de / et d'où partent les chemins. 
                        nom_item1b_1 = detectsalahhashtag(Item1b.get_name())
                        if nom_item1b_1 == nom_file1b:
                            Content1b = Item1b.get_content()
                    #On va dans le dossier de sortie: "dossier_sortie1/"+nom_sansext1b
                    #On crée un fichier de nom le playorder: current_playorder
                    #chemin du dossier pas en path forcément. 
                    Dossier1b = "dossier_sortie1/"+nom_sansext1b
                    #nom du fichier
                    Nom_fichier_final1b = str(current_playorder)
                    Chemin_complet1b = os.path.join(Dossier1b, Nom_fichier_final1b) 
                    # Le mode 'w' (write) crée le fichier s'il n'existe pas ou l'écrase s'il existe. 
                    # C'est du binaire donc 'wb'
                    with open(Chemin_complet1b, 'wb') as F1b: 
                        #On met le contenu dedans: le contenu: content1b
                        F1b.write(Content1b) 
                    #Et c'est bon
                    #On rajoute à dic1 les infos sur ce fichier. le texte d’entrée A. et le nom du fichier B.b.
                    #On récupère A.
                    #C'est le texte de la balise a. Soit ici: sous_sous_balise1d
                    AA1b =  sous_sous_balise1b.get_text()
                    #On récupère B.b.
                    BBb1b = nom_file1b
                    #On les met dans une liste et on ajoute cette liste dans le dictionnaire dic1. 
                    #Il faut aller voir la clé: nom du titre du livre sans extension: nom_sansext1b.
                    #On ajoute alors à la valeur associée à cette clé: .append([A.,B.b.])
                    dic1[nom_sansext1b].append([AA1b,BBb1b])
                    #On remplit dic2. 
                    #Comme clé on a le titre originel du livre. Le titre de son dossier epub.  
                    #Sans extension bien sur: nom_sansext1b
                    #Pour chaque clé livre on a alors un dictionnaire avec comme clés: les fichiers. 
                    #Les clés se sont leurs titres, donc les navpoint. Et les valeurs sous forme de liste:
                    dic2[nom_sansext1b][current_playorder]=[cc1b,BBb1b,current_playorder]
            
        except Exception as e:
            #On ajoute à la Liste des mauvais livre le nom complet du fichier avec avant : "ce fichier ne respecte pas les normes epub2 et epub3: "
            L_mauvais_livres.append("ce fichier ne respecte pas les normes epub2 et epub3: "+ fichier1a.name)
    
    #On retourne les dictionnaires et la liste des mauvais livres. Et Liste avec le nom des fichiers sans extensions: L_fichiers1a
    return dic1, dic2, L_mauvais_livres, L_fichiers1a


"""TEST"""

#dictionnaire1, dictionnaire2, Liste_mauvais, L_livres_sansext = f1("epubs")
#print(dictionnaire1)
#print(dictionnaire2)
    
