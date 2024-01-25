#Leggiamo il file e carichiamolo in un DataFrame, aggiungendo i nomi di colonna — che si trovano nel file
#.names — come parametro di pd.read_csv() • Stampiamo le prime cinque righe e le ultime dieci • Stampiamo un
#riepilogo dei descrittori statistici del dataset

import pandas as pd

file_name ="./iris/iris.data"
data = pd.read_csv(file_name, names= ["sepal length","sepal width","petal length","petal width","class"])


print(data.head())

print(data.tail(10))

print(data.describe())