#Scarichiamo il dataset stockdata da 
#Estraiamo i dati della colonna MSFT relative all'andamento delle azioni di Microsoft,e visualizziamolo mediante pyplot 
#Estraiamo le prime 5 righe della colonna MSFT e della colonna date, e usiamoli come ascisse e ordinate
# su un grafico mediante pyplot 
#Facciamo lo stesso per le ultime 5 righe del dataset

import pandas as pd
import matplotlib.pyplot as plt
import humanize as h

file_name ="./stockdata.csv"
stock = pd.read_csv(file_name)

dati_msft = stock['MSFT']

print(dati_msft)
plt.plot(dati_msft)

plt.show()

dati2 = stock[['MSFT','Date']].head(5)
#print(dati2)

plt.plot(dati2['Date'],dati2['MSFT'],marker = "o",color='red')

plt.xlabel('MSFT')
plt.ylabel('Date')
plt.title('Stockdata')

plt.show()

dati3 = stock[['MSFT','Date']].tail(5)


plt.plot(dati3['Date'],dati3['MSFT'],marker = "o",color='red')

plt.xlabel('MSFT')
plt.ylabel('Date')
plt.title('Stockdata')

plt.show()






