#Visualizzare un grafico con il numero di passeggeri di ogni classe di imbarco 
#Fare la stessa cosa per la colonna alive • 
#Qual era la distribuzione delle tariffe (fare)? •
#Riusciamo a vedere la distribuzione delle età dei passeggeri rispetto alla classe di imbarco? 
#Proviamo con un boxplot e con uno swarmplot • 
#Visualizziamo un boxplot e un lmplot rispetto alle colonne fare e survived; che cose ne deduciamo?

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic)



#passeggeri = titanic[['survived','pclass']].groupby(['pclass']).count()
#print(passeggeri)

#sns.barplot(data=passeggeri, x="pclass", y="survived")
#plt.show()

sns.countplot(data=titanic, x="pclass")
plt.show()

sns.countplot(data=titanic, x="alive")
plt.show()

sns.displot(titanic['fare'])
plt.show()

sns.boxplot(data=titanic,x='pclass',y='age')
plt.show()

sns.swarmplot(data=titanic,x='pclass',y='age')
plt.show()

sns.boxplot(data=titanic,x='fare',y='survived')
plt.show()

sns.lmplot(data=titanic,x='fare',y='survived')
plt.show()