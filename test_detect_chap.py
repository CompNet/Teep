# Le nom du livre que l'on va faire passé dans 4. 
nom_livre = "_OceanofPDF.com_We_Ride_Upon_Sticks_-_Quan_Barry"

# On va s'ocupper du 1.
# On importe le fichier
import récuperation_des_données
# On applique la fonction f1 de récuperation_des_données sur le dossier epubs
# On en récupère nos deux dictionnaires. 
dic1, dic2, liste_mauvais_livres, L_nom_livres_sansext = récuperation_des_données.f1("epubs")

#print(dic1,dic2,liste_mauvais_livres,L_nom_livres_sansext)
print(dic1[nom_livre])

"""
# On va s'occcuper du 2.
# transformation_en_textes.py
# On créer la fonction: transformation_totale qui est sur la partie 1. 
# Et qui prend un dossier d'entrée total et un dossier de sortie total en variables: dossier_entrée_total,dossier_sortie_total
# Ceux sont les noms des dossiers par leurs paths.

# On lance la fonction avec "dossier_sortie1" comme entrée et "dossier_sortie2" comme sortie dans transformation_totale
import transformation_en_textes
transformation_en_textes.transformation_totale("dossier_sortie1","dossier_sortie2")"""


# On va s'occuper du 3. 
# On a que le 3. doit prendre en entrée le dictionnaire 1 et L_nom_livres_sansext et en sortie le dictionnaire3.
import détecteur_de_référence
dic3 = détecteur_de_référence.fabrication_dictionnaire3(dic1,L_nom_livres_sansext)

print(dic3[nom_livre])

# On va s'occuper du 4.
# fprincipale5(dict2,dict3,L_nom_livres_sansext):
# Elle ne retourne rien elle ne fait que des modifications sur les fichiers. 
#On importe le fichier code
# Pour: "_OceanofPDF.com_The_Devil_Takes_You_Home_-_Gabino_Iglesias"
import détecteur_chap
dic3_final = détecteur_chap.fprincipale5({nom_livre:dic2[nom_livre]},
                                         {nom_livre:dic3[nom_livre]},
                                         [nom_livre])

print(dic3_final[nom_livre])