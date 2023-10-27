import pandas as pd
import numpy as np
from sklearn import preprocessing
import missingValues
""" 

burada missingValues.csv dosyasındaki ulke kolonunda yer alan us,tr,fr verilerini
tek tek bir kolon haline getirmek için gerekli kodu yazdık

"""

data = pd.read_csv(r"C:/Users/Ayhan/Desktop/ml/missingDatas.csv")


country = data.iloc[:,0:1].values


labelEncoder = preprocessing.LabelEncoder()

country[:,0] = labelEncoder.fit_transform(data.iloc[:,0])

print(country)

ohe = preprocessing.OneHotEncoder()

country = ohe.fit_transform(country).toarray()

print(country)


result = pd.DataFrame(data=country, index=range(22), columns=["fr", "tr", "us"])
result2 = pd.DataFrame(data= missingValues.age, index= range(22), columns=["boy","kilo","yas"])

gender = data.iloc[:,-1].values

result3 = pd.DataFrame(data=gender, index=range(22), columns=["cinsiyet"])

s = pd.concat([result, result2], axis=1)

print(s)

s2 = pd.concat([s,result3], axis=1)

print(s2)