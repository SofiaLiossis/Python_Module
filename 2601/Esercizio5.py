#Quanti ponti c'erano sulla nave? 7
#Ci sono dati mancanti? Dove? Quanti? Che logica potremmo usare per gestirli? 
#Tramite seaborn visualizziamo un lmplot sulle colonne age e fare; che cosa stiamo guardando?
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic)

ponti = titanic['deck'].nunique()
print(ponti)


print(titanic.isnull().sum())

sns.lmplot(data=titanic, x="age", y="fare")
plt.show()