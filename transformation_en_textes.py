#Il faut avoir calibre de téléchargé sur notre pc. on va alors utiliser des dossiers de calibre.
#On va utiliser le module python subprocess qui permet justement d’utiliser d’autres process i.e. programmes que python pour faire tourner notre code.















# 3.

#importation
import subprocess
import os


#On crée la fonction qui transforme un fichier html en texte.
def convert_html_to_txt(input_file,nom_dossier_sortie,dossier_sortie_total):
    
    try:
        #On peut faire en sorte d'avoir un chemin de sortie pour une fonction. Lorsque l’on crée un fichier. 
        #On peut faire en sorte que le fichier de sortie ait un certain nom:
        #le nom du fichier de sortie est alors celui de celui d’entrée dans la fonction avec à la fin à la place de .txt un .html.
        nom_fichier = os.path.basename(input_file).replace('.html', '.txt')
        #ici le chemin de sortie envoie vers un dossier de sortie
        #définition du dossier de sortie:
        dossier_sortie = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/" + dossier_sortie_total + "/" +nom_dossier_sortie)
        #test
        print(dossier_sortie.exists())
        print(nom_dossier_sortie)
        chemin_sortie = os.path.join(dossier_sortie, nom_fichier)
        #pour cette fonction
        #'ebook-convert': Chemin vers l'exécutable ebook-convert
        # Sur Linux/macOS, il est souvent dans le PATH.
        # Sur Windows, il est généralement dans "C:\Program Files\Calibre2\ebook-convert.exe"
        #Nous il est bien à cet endroit soit:
        chemin_ebook_convert = "C:/Program Files/Calibre2/ebook-convert.exe"
        subprocess.run([chemin_ebook_convert, input_file, chemin_sortie]) 
        print(f"Conversion réussie")
    # dans le cas où cela ne marche pas. On retourne alors l’erreur
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la conversion : {e}")



















# 2. 

#toutes les importations
from pathlib import Path
import os
import shutil


#fonction transformation
def transformation(nom_dossier_entrée,nom_fichier,nom_dossier_sortie,dossier_entrée_total,dossier_sortie_total):
    #récupérations 
    dossier = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/" + dossier_entrée_total + "/" +nom_dossier_entrée)
    #on récupère les fichiers:
    liste_fichiers = dossier.glob(nom_fichier)
    for fichier in liste_fichiers:
        #créer un dossier vide pour lui et le copier dedans

        #créer le dossier
        # Définir le chemin du dossier que vous voulez créer
        # On le met : C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_temporaire
        chemin = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_temporaire")
        # Créer le dossier: dossier_temporaire
        # parents=True : crée aussi les dossiers parents s'ils n'existent pas
        # exist_ok=True : ne renvoie pas d'erreur si le dossier existe déjà
        chemin.mkdir(parents=False, exist_ok=False)

        #copier notre fichier dans ce dossier
        #on récupère le contenu: contenu_temporaire
        with open(fichier, "r", encoding="utf-8") as f:
            contenu_temporaire = f.read()
        #on le colle
        dossier_temporaire = "C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_temporaire"
        #nom du fichier, même nom que notre fichier au dessus. avec l'extension donc.Cra on peut avoir plusieurs extensions one ne peut donner un nom générique comme a.html.
        #justement on va résoudre le problème qu'il dit qu'il ne sait pas gérer du xhtml et du htm en forcant dans ce copier coller les passgaes du htm et du xhtml au html. 
        #mais il faut garder le nom du fichier on sait jamais. Il faut alors le répercuter partout. 
        nom_ancien_fichier = fichier.stem
        nom_fichier = nom_ancien_fichier+".html"
        chemin_complet = os.path.join(dossier_temporaire, nom_fichier) 
        # Le mode 'w' (write) crée le fichier s'il n'existe pas ou l'écrase s'il existe. 
        with open(chemin_complet, 'w', encoding='utf-8') as f: 
            #on y copie donc le contenu temporaire: contenu_temporaire
            f.write(contenu_temporaire) 

        #le traiter dans notre fonction
        #conversion du fichier en textes:
        #importation du fichier
        #On met son nouveau path
        fichier = "C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_temporaire/"+nom_fichier
        convert_html_to_txt(fichier,nom_dossier_sortie,dossier_sortie_total)
        #puis supprimer le dossier avec le fichier dedans. 
        # on veut supprimer: dossier_temporaire = "C:/Users/USER/Fichiers de Travail/stage 2A/Projet/traitement des livres/dossier_temporaire"
        dossier_a_supprimer = "C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/dossier_temporaire"
        shutil.rmtree(dossier_a_supprimer)


























# 1. 

#toutes les importations
import os
from pathlib import Path 

def transformation_totale(dossier_entrée_total,dossier_sortie_total):
    #on va parcourir le dossier_entrée_total
    #chemin du dossier où il y aura les sous dossiers
    dossier_parent = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/"+dossier_entrée_total)
    # Utilisation de os.scandir pour aller dans le dossier parent et ne récupérer que ce qui est un dossier: .is_dir().
    #On obtient alors la liste des paths des sous dossiers: 
    sous_dossiers = [f.path for f in os.scandir(dossier_parent) if f.is_dir()]
    #mais l’écriture est mauvaise
    sous_dossiers = [ Path(d) for d in sous_dossiers]
    #pour chaque sous dossier: sous_dossier
    for sous_dossier in sous_dossiers:

        #On crée un sous dossier correspondant de même nom dans dossier_livres_textes qui comptient tous les fichiers textes dans le même ordre. 
        #On crée un sous dossier correspondant de même nom dans dossier_livres_textes
        #On récupère le nom du dossier 
        nom_dossier = sous_dossier.name
        #On enlève la référence à Oceanopdf dans le nom des dossiers. on enlève les 16 premiers caractères du nom. donc de l'indice 0 à 15.
        #avec du slicing [16:]
        #Il faut en créer une nouvelle variable car si on garde l'ancienne quand on passera à transformation plus tard on n'aura plus le bon nom de fichier.
        #et seulement pour les Oceano
        #si le nom du dossier est bien celui d'un Oceano on le renomme
        if nom_dossier[:15] == "_OceanofPDF.com_" :
            nom_dossier_sans_Oceano = nom_dossier[16:]
        #Sinon on ne fait rien le nom du dossier est le même sans Oceano:
        else:
            nom_dossier_sans_Oceano =  nom_dossier
        #On en crée une nouvelle version dans dossier_livres_textes
        # Définir le chemin du dossier que vous voulez créer
        # Par exemple : "dossier_parent/nouveau_dossier"
        chemin1_sous_dossier = Path("C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/" + dossier_sortie_total + "/" +nom_dossier_sans_Oceano)
        # Créer le dossier
        # parents=True : crée aussi les dossiers parents s'ils n'existent pas
        # exist_ok=True : ne renvoie pas d'erreur si le dossier existe déjà
        chemin1_sous_dossier.mkdir(parents=True, exist_ok=True)

        #On parcourt sous_dossier:
        #on récupère sous_dossier grâce à son path: sous_dossier
        #récupérations 
        dossier = Path(sous_dossier)
        #on récupère les fichiers:
        liste_fichier_sous_dossier = dossier.glob("*")
        for fichier in liste_fichier_sous_dossier:

            #on transforme chaque dossier en fichier texte et on le met dans le sous dossier correspondant de même nom dans dossier_livres_textes
            #on appel la fonction: transformation
            #qui prend en variable le nom du sous dossier de dossier_livres_textes/ + dossier_entrée_total (c'est le même) et le nom avec extension du fichier à transférer
            #i.e. nom_dossier et fichier.name
            nom_fichier = fichier.name
            """jusque là ça marche"""
            transformation(nom_dossier,nom_fichier,nom_dossier_sans_Oceano,dossier_entrée_total,dossier_sortie_total)





"""
I. POUR LE TEST SUR LES PRMIERS BASE DE DONN2ES DE LIVRES

On a un problème il ne semble pas lire le xhtml
1. On va déjà essayer avec du html il est censé le reconnaître.
a. il faut déjà résoudre le problème de calibre: à chaque fois il va nous chercher tout le livre. 
J'ai beau lui donner seulement un chapitre dans un livre il récupère tout l'epub qui va avec et il me le transforme tout ça en texte.
Ce qu'il faut donc faire c'est à chaque fois:
prendre chaque fichier
créer un dossier vide pour lui et le copier dedans
le traiter dans notre fonction
puis supprimer le dossier avec le fichier dedans. 
#Comme ça calibre n'essaye de récupérer tout l'epub global. 
on va résoudre le problème qu'il dit qu'il ne sait pas gérer du xhtml et du htm en forcant dans ce copier coller les passages du htm et du xhtml au html. 
On teste avec du html. Ca marche! On va juste tester avec du xhtml pour être sur. 
avant ça: histoire de garder le nom du fichier. 
On va juste tester avec du xhtml pour être sur. 
ça marche!!!!
#On apprendra à supprimer le dossier quand cela marchera. 
#On créer une boucle qui parcourt tous les dossiers, tous les fichiers, et le code de téléchargment on le transforme en fonction.
#Il faudra faire gaffe pour chaque livre i.e. pour chaque sous dossier du dossier_entrée_total:
#créer un sous dossier correspondant de même nom dans dossier_livres_textes qui comptient tous les fichiers textes dans le même ordre. 
#On enlève la référence à Oceanopdf dans le nom des dossiers. on enlève les 16 premiers caractères du nom.
Ainsi in fine on ne touche pas aux dossier originaux en html. 
On va mettre les options pour que chaque nouveau dossier n'est pas à le supprimer à chaque début de test. On lmet l'option s'il existe déjà tu n'en recrée pas un. 
#On code l'itération
#On code la fonction transformation et convert_html_to_txt
il n'y a qu'à faire en sorte que la fonction prenne en plus du fichier comme variable le nom du dossier de sortie.
Et de customiser alors le chemin de soprtie dans la fonction. 
Ca marche.
On voudrait juste maintenant qu'il nous parcoure nos sous dossier dans un ordre un peu logique. 
C'est logique c'est l'ordre alphabétique mais pas le même que celui de nos dossiers. 
En soit ce n'est pas très rave si l'ordre n'est pas le même que celui de notre dossier au dessus. 
Cela serait un bordel de faire en sorte que les suivent le mêm ordre alphabétique. Cela prendrait du temps pour rien.
J'aimerai juste m'assurer que quand je veux créer un nouveau fichier si celui-ci existe déjà pas de problèmes. Le nouveau le remplace ou on ne fait rien. 
C'est bon ça marche.
#On test
c'est bon
#On vérifie l'ordre
c'est bon.
Si on interrompt le script bien penser à supprimer le dossier temporaire.
"""

"""
II. MISE EN PLACE SUR LES LIVRES FINAUX

On va devoir travailler dans total.py. 
on a que désormais les titres ne commencent pas tous pas Oceanopdf.. Donc faire un if. 
Il faudra garder le fait que l'on nous dise quel est le dossier de travail en cour spour savoir où on en est. 
On regarde les premiers résultats. On arrête le code.
Puis on lance définitivement, cela devrait être bon. 
"""