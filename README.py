#MARWA Zeghoudi \ Master 1 microbiologie fondamentale \ 12-12-2025
#HANANE Yahoui
#SARRA Imouloudene 
#NOURHANE Bedai
#SELSABILE Benchadli

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
