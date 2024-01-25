#Troveremo un file .data, che è un CSV, e un file .names con i metadati; questa versione del dataset non ha i nomi di colonna.
#Leggiamo il file e carichiamolo in un DataFrame mediante pd.read_csv() senza utilizzare altri parametri 
#Stampiamo le prime cinque righe • Stampiamo i nomi di colonna: descrivono cosa c'è nella colonna relativa?


import pandas as pd

file_name ="./iris/iris.data"
data = pd.read_csv(file_name)
print(data)

print(data.head())

print(data.columns)  #Non descrivono cosa c'è nella relativa colonna
