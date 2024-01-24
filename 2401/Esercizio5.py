#Esercizio 5
#Abbiamo la seguente matrice:
#Creiamo un ndarray con gli stessi valori. Ci sono due modalità: inizializzare un array e poi
#inserire i valori nelle posizioni adatte, oppure creare una lista di liste e poi effettuare un casting.

import numpy as np

# Creare una lista di liste con gli stessi valori
lista = [[1, 1, 1, 1], [5, 1, 1, 1], [20, -4, 0, 42]]
arr = np.array(lista)
print(arr)

