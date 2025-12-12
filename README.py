#MARWA Zeghoudi \ Master 1 microbiologie fondamentale \ 12-12-2025
#HANANE YAHIAOUI 
#SARRA Imouloudene 
#NOURHANE Bedai
#SHAHINAZ Benchadli

import pandas as pd

# Données : Séquences ADN, Longueur, Pourcentage de GC :
data = {
"Séquence" : ["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
"Longueur" : [12,12,12,10,11,10,10],
"Pourcentage GC" : [50,60.67,58.33,40,45.45,60,50]
}

#Creation d'un DataFrame :
df = pd.DataFrame(data)
print("-------------creation et affichage-------------","\n")

#1)Affichage de tableau:
print("Tableau des séquences d'ADN : ")
print(df,"\n")

#2.a)opération sue les tableaux :
print("-------------Opération-------------","\n")
#2.b)Sélectionner la colonne "Longueur":
lng = df["Longueur"]
print(lng,"\n")

#3)Filtrer les séquences dont la longueur est supérieure à 10 :
print("-------------Filtrage de langueur des séquences > 10-------------","\n")
filtered_df = df[df["Longueur"]>10] print(filtered_df)
print("\n") 

#4) Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule : 
print("-------------calcul de la moyenne-------------","\n")   
moyenne = df["Pourcentage GC"].mean() print(f"Pourcentage moyen GC :[{moyenne :.3f}%")
print("\n") 

#5) Ajouter une colonne "catégorie GC" avec des calculs :
print("-------------Ajouter d'une colonne-------------","\n") 
df["Catégorie GC"] = df["Pourcentage GC"].apply(lambda x: "Riche" if x > 55 else "Moyen" if 45 <= x <= 55 else "Faible")
print(df)
print("\n")
#6)Ajouter une colonne donnant le nombre de G dans chaque séquence: 
df["Nombre de G"] = df["séquence"].str.count("G") 
print("-------------Nombre de G-------------","\n") 
print (df,"\n") 
