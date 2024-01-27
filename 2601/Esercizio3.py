#Utilizzando i metodi di rappresentazione grafica dei DataFrame, visualizziamo l'andamento di tutte le azioni sullo stesso grafico 
#Tramite pyplot, spostiamo la legenda in basso a destra

import pandas as pd
import matplotlib.pyplot as plt

file_name ="./stockdata.csv"
stock = pd.read_csv(file_name)

#print(stock)

andamento = stock.plot(x='Date',y=['MSFT','IBM','SBUX','AAPL','GSPC'],color='r',linewidth= 1)

plt.xlabel('Data')
plt.ylabel('Valore Azioni')
plt.title('Andamento Azioni')

plt.legend(loc='lower right')

plt.show()

