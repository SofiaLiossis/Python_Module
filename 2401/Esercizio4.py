#Esercizio 4
#In una catena di montaggio abbiamo una struttura metallica di 28.75 cm di lunghezza; per assicurarne la stabilità,
#è necessario inserire 15 rivetti, dei quali uno all'inizio e uno alla fine, e tutti quanti separati dalla stessa
#distanza; come possiamo calcolare i punti esatti in cui inserire i rivetti tramite NumPy?


import numpy as np

lungh_metallo = 28.75  
num_rivetti = 15  

# Calcolo dei punti esatti in cui inserire i rivetti
punti_rivetti = np.linspace(0, lungh_metallo, num_rivetti)

# Visualizzazione dei punti esatti dei rivetti
print(punti_rivetti)






