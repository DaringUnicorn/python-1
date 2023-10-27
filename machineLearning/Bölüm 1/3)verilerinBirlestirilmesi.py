
# kütüphaneler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
# veri yükleme

veriler = pd.read_csv("veriler.csv")


# veri ön işleme
boy = veriler[["boy"]]
boy2 = veriler["boy"]
print(f"veriler içerisindeki boy kolonu : \n{boy}\ntype : \n{type(boy)}")

print(f"veriler içerisindeki boy kolonu : \n{boy2}\ntype : \n{type(boy2)}")


# eksik veriler

# eksikler bulunan kolonun var olan değerlerinin ortalaması alınıp eksik hücrelere yerleştirilir

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
yas = veriler.iloc[:,1:4].values

print(yas)

imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])

print(yas)



# nominal etiket değerlerini kolon şekliene getirme (kategorik veri dönüşümü)

ulke = veriler.iloc[:,0:1].values
print(ulke)

labelEncoder = preprocessing.LabelEncoder()

ulke[:,0] = labelEncoder.fit_transform(veriler.iloc[:,0])

print(ulke)


oneHotEncoder = preprocessing.OneHotEncoder()

ulke = oneHotEncoder.fit_transform(ulke).toarray()

print(ulke)

ulkeDf = pd.DataFrame(data=ulke, index=range(22), columns=["fr","tr","us"])

print(ulkeDf)

yasDf = pd.DataFrame(data=yas, index=range(22), columns=["boy","kilo","yas"])
print(yasDf)

cinsiyet = veriler.iloc[:,-1].values


cinsiyetDf = pd.DataFrame(data=cinsiyet, index=range(22), columns=["cinsiyet"])

print(cinsiyetDf)

prepDf = pd.concat([ulkeDf,yasDf],axis=1)
print(prepDf)

finalDf = pd.concat([prepDf,cinsiyetDf],axis=1)

print(finalDf)