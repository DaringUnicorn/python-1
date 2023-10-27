import pandas as pd
import numpy as np

veriler = pd.read_csv("C:/Users/Panda/OneDrive/Masaüstü/desktop/python - Kopya/machineLearning/Bölüm 2/veriler.csv")

print(veriler)

boy = veriler[["boy"]]


print(boy)

boyKilo = veriler[["boy","kilo"]]



from sklearn.impute import SimpleImputer

simpleImputer = SimpleImputer(missing_values=np.nan, strategy="mean")

yas = veriler.iloc[:,1:4].values

simpleImputer = simpleImputer.fit(yas[:,1:4])



yas[:,1:4] = simpleImputer.transform(yas[:,1:4])

print(yas)