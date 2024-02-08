
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('C:/Users/lioss/OneDrive/Desktop/Python/Python_Module/0502/dataset_climatico.csv')
#Pulire i dati per rimuovere eventuali valori mancanti o errati:
df.dropna(inplace=True)

#Applicare la normalizzazione Z-score alla temperatura_media, precipitazioni, umidità e velocità_vento per standardizzarle:
colonne_da_normalizzare = ["temperatura_media", "precipitazioni", "umidita", "velocita_vento"]
media = df[colonne_da_normalizzare].mean()
deviazione_standard = df[colonne_da_normalizzare].std()
df[colonne_da_normalizzare] = (df[colonne_da_normalizzare] - media) / deviazione_standard

print(df.head())

#Calcolare statistiche descrittive (media, mediana, deviazione standard) per ogni variabile.
descrizione = df.describe()

print(descrizione)

df.hist(bins=20, figsize=(12, 8))
plt.suptitle('Distribuzione delle Variabili Normalizzate', y=0.95)
plt.show()


#Creare grafici (istogrammi, box plots) per visualizzare la distribuzione:
df["data_osservazione"] = pd.to_datetime(df["data_osservazione"]).dt.date

#df.set_index("data_osservazione", inplace=True) 
#df.resample("M")["temperatura_media"].mean().plot(kind="line")
#plt.title("Temperatura mensile") 
#plt.xlabel("Data") 
#plt.ylabel("Temperature tot") 
#plt.show()

for colonna in colonne_da_normalizzare:
    plt.figure(figsize=(10, 4))
    # Istogramma
    plt.subplot(1, 2, 1)
    sns.histplot(df[colonna], bins=30, kde=True)
    plt.title('Istogramma di ' + colonna)
    # Box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[colonna])
    plt.title('Box plot di ' + colonna)
    plt.show()

    #Utilizzare una heatmap per visualizzare la correlazione tra le diverse variabili meteorologiche. 
    #Identificare eventuali correlazioni significative (es. tra temperatura e umidità).

matrice_correlazione = df[colonne_da_normalizzare].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_correlazione, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Matrice di Correlazione tra Variabili Meteorologiche')
plt.show()

plt.figure(figsize=(8, 6))
sns.regplot(x=df["temperatura_media"], y=df["precipitazioni"])
plt.title('Grafico di Regressione tra Temperatura Media e Precipitazioni')
plt.xlabel('Temperatura Media')
plt.ylabel('Precipitazioni')
plt.show()


                                    




