#Estraiamo le prime 20 istanze della colonna AAPL delle azioni di Apple, e visualizziamo il grafico tramite pyplot, in modo che:
#il grafico sia rosso 
#la linea sia tratteggiata
#vi sia un pallino come marker
#l'asse delle ascisse si chiami "Data" 
#l'asse delle ordinate si chiami "Valore" 
#il titolo del grafico sia "Azioni Apple" 
#il markerfacecolor sia nero 
#la linea abbia spessore uguale a 2

import pandas as pd
import matplotlib.pyplot as plt

file_name ="./stockdata.csv"
stock = pd.read_csv(file_name)

dati_a = stock['AAPL'].head(20)
#print(dati_a)

plt.plot(dati_a,color='r', linestyle='--', marker='o', markerfacecolor='k', linewidth=2)

plt.xlabel('Data')
plt.ylabel('Valore')
plt.title('Azioni Apple')

plt.show()
