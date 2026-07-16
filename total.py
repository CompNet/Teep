# On va s'ocupper du 1.
# On importe le fichier
import récuperation_des_données
# On applique la fonction f1 de récuperation_des_données sur le dossier epubs
# On en récupère nos deux dictionnaires. 
# test
dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext = récuperation_des_données.f1("epubs")
print("Etape 1 passée")


"""
print("Etape 2 commence")
# On va s'occcuper du 2.
# transformation_en_textes.py
# On créer la fonction: transformation_totale qui est sur la partie 1. 
# Et qui prend un dossier d'entrée total et un dossier de sortie total en variables: dossier_entrée_total,dossier_sortie_total
# Ceux sont les noms des dossiers par leurs paths.

# On lance la fonction avec "dossier_sortie1" comme entrée et "dossier_sortie2" comme sortie dans transformation_totale
import transformation_en_textes
transformation_en_textes.transformation_totale("dossier_sortie1","dossier_sortie2")
print("Etape 2 passée")"""


print("Etape 2.1 commence")
# On va s'occuper du 2.1:
# detect_bet.py
# f21(dossier_sortie2,dossier_sortie3,dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext)
import detect_bet2
dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext = detect_bet2.f21("dossier_sortie2","dossier_sortie3",dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext)
print("Etape 2.1 passée")


print("Etape 3 commence")
# On va s'occuper du 3. 
# On a que le 3. doit prendre en entrée le dictionnaire 1 et L_nom_livres_sansext et en sortie le dictionnaire3.
import détecteur_de_référence
dic3 = détecteur_de_référence.fabrication_dictionnaire3(dic1,L_nom_livres_sansext)
print("Etape 3 passée")

# Test
a = dic3["_OceanofPDF.com_True_love_experiment_-_Christina_Lauren"]
b = dic3["_OceanofPDF.com_Wicked_and_the_Wallflower_-_Sarah_MacLean"]

print("Etape 3.1 commence")
# On va s'occuper du 3.1
# On a que le 3.1 doit prendre en entrée: "dossier_sortie3","dossier_sortie3_1",dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext.
# Et en sortie: dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansex
import detect_bet3
dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext = detect_bet3.f31("dossier_sortie3","dossier_sortie3_1",dic1, dic2, dic3, liste_mauvais_livres, L_nom_livres_sansext)
print("Etape 3.1 passée")


print("Etape 4 commence")
# On va s'occuper du 4.
# fprincipale5(dict2,dict3,L_nom_livres_sansext):
# Elle ne retourne rien elle ne fait que des modifications sur les fichiers. 
#On importe le fichier code
import détecteur_chap
dic3_final = détecteur_chap.fprincipale5(dic2,dic3,L_nom_livres_sansext)
print("Etape 4 passée")


print(dic3_final,liste_mauvais_livres)

# On veut en récupérer:
# Les clés de dic3_final
clés = dic3_final.keys() 
# Le nombre de ces sous clés de dic3_final
nb_sous_clés = 0
nb_sous_clés0 = 0
nb_sous_clés1 = 0
nb_sous_clésmoins1 = 0
# On les parcourt, les clés de dic3_final:
for clé in clés:
    # On en parcourt les sous clés:
    sous_clés = dic3_final[clé].keys()
    for sous_clé in sous_clés:
        # A chaque fois:
        valeur = dic3_final[clé][sous_clé]
        # Le nombre de sous clés de dic3_final égales à 0
        if valeur == 0:
            nb_sous_clés0 += 1
        # Le nombre de sous clés de dic3_final égales à 1
        if valeur == 1:
            nb_sous_clés1 += 1
        # Le nombre de sous clés de dic3_final égales à -1
        if valeur == -1:
            nb_sous_clésmoins1 += 1
        # +1 pour le compteur de nombre de ces sous clés de dic3_final
        nb_sous_clés += 1

print("nb_sous_clés")
print(nb_sous_clés)
print("nb_sous_clés0")
print(nb_sous_clés0)
print("nb_sous_clés1")
print(nb_sous_clés1)
print("nb_sous_clésmoins1")
print(nb_sous_clésmoins1)
print("liste_mauvais_livres")
print(len(liste_mauvais_livres))
print("L_nom_livres_sansext")
print(len(L_nom_livres_sansext))


