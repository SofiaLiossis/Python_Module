#Esercizio 2
#Trasformiamo la lista in un array NumPy:
#Come facciamo per accedere ai singoli elementi?

import numpy as np

mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9],[10, 11, 12, 13, 14]]
mat = np.array(mat)
elemento = mat[1, 2]  # Accede all'elemento nella seconda riga e terza colonna
print(elemento)       # Output: 7