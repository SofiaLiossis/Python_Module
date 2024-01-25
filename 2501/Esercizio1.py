#Tra i vari dataset presenti, ce n'è uno che contiene diverse qualità di vini e le misure di diverse proprietà organolettiche:
#wine.csv; Effettuiamo calcoliamo le informazioni statistiche base (numerosità, modie, mode, mediane, quartili, ecc) 
#sulle colonne numeriche usando python 

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

#file_name ="C:/Users/lioss/OneDrive/Desktop/Python/Python_Module/2501/wine.csv"
file_name ="./wine.csv"
wine = pd.read_csv(file_name)


for col in wine.columns:
    print("colonna:", col)
    data_col = wine[col]
    if is_numeric_dtype(wine[col]):
        media=np.mean(data_col)
        mediana = np.median(data_col)
        moda = data_col.mode()[0]
        percentile25= np.percentile(data_col,25)
        percentile75= np.percentile(data_col,75)
        
        print("Media:",media,"Mediana:",mediana,"Moda:",moda,"Percentile25:",percentile25,"Percentile75",percentile75)

    else: 
        print("Colonna non numerica")    

        







