#Alternativa con Pandas

import numpy as np
import pandas as pd


#file_name ="C:/Users/lioss/OneDrive/Desktop/Python/Python_Module/2501/wine.csv"
file_name ="./wine.csv"
wine = pd.read_csv(file_name)

media= wine.mean(axis=0,numeric_only=True)
mediana= wine.median(axis=0,numeric_only=True)
moda= wine.mode(axis=0,numeric_only=True)
quartile25= wine.quantile(axis=0,q=0.25,numeric_only=True)
quartile75= wine.quantile(axis=0,q=0.75,numeric_only=True)

print("Media:\n",media)
print("Mediana:\n",mediana)
print("Moda:\n",moda)
print("Quartile25:\n",quartile25)
print("Quartile75:\n",quartile75)