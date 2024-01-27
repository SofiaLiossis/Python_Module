#Scarichiamo il dataset elections da
#Con un grafico a barre confrontiamo i voti totali presi dai tre candidati (come somma di tutti i distretti)
#Con un grafico a barre confrontiamo il numero di votanti per ogni distretto • 
#Visualizzare un grafico a barre comparativo dove si confrontano i voti presi nei primi 4 distretti per ogni candidato
#Visualizzarlo sia in formato appaiato che impilato (stacked) e salvare entrambi i grafici su disco in alta risoluzione

import pandas as pd
import matplotlib.pyplot as plt

file_name ="./election.csv"
elezioni = pd.read_csv(file_name)
#print(elezioni)

tot_coderre = elezioni['Coderre'].sum()
tot__bergeron = elezioni['Bergeron'].sum()
tot_joly = elezioni['Joly'].sum()
print("Coderre:",tot_coderre,"Bergeron:",tot__bergeron,"Joly:",tot_joly)

tot = elezioni[['Coderre','Bergeron','Joly']].sum() 
print(tot)

plt.bar(['Coderre','Bergeron','Joly'],tot)
plt.show()

plt.bar(elezioni['district'],elezioni['total'])
plt.show()


voti = elezioni[['district','Coderre','Bergeron','Joly']].head(4)
print(voti)

voti.plot(x='district',y =['Coderre','Bergeron','Joly'],kind="bar")
plt.savefig("voti.png", dpi=600)

voti.plot(x='district',y =['Coderre','Bergeron','Joly'],kind="bar",stacked=True)
plt.savefig("voti_stacked.png", dpi=600)