#Esercizio 3
#Abbiamo il seguente array NumPy:
#Lo ridimensioniamo mediante il metodo .reshape():
#Quante dimensioni ha il nuovo array? Come facciamo per accedere ai singoli elementi?


import numpy as np

linear_data = np.array([x for x in range(27)])
reshaped_data = linear_data.reshape((3, 3, 3)) #ridimensionamento;ha 3 dimensioni con una dimensione di 3.
print(reshaped_data)

elemento = reshaped_data[1,1,2]                #Accede all'elemento nella seconda dimensione,seconda riga,terza colonna.
print(elemento)                                # Output: 14





