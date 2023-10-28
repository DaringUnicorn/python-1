# -*- coding: utf-8 -*-

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

ulke = veriler.iloc[:,0:1].values

print(ulke)



from sklearn import preprocessing

labelEncoder = preprocessing.LabelEncoder()

ulke[:,0] = labelEncoder.fit_transform(veriler.iloc[:,0])
                                       
print(ulke)

ohe = preprocessing.OneHotEncoder()

ulke = ohe.fit_transform(ulke).toarray()

print(ulke)

sonuc = pd.DataFrame(data=ulke, index=range(22), columns=["fr","tr","us"])

print(sonuc)
sonuc2 = pd.DataFrame(data=yas, index=range(22), columns=["boy","kilo","yas"])


cinsiyet = veriler.iloc[:,-1].values

sonuc3 = pd.DataFrame(data=cinsiyet, index=range(22), columns=["cinsiyet"])

print(sonuc3)


cinsiyetColumn = veriler.iloc[:,-1].values

cinsiyetColumn = labelEncoder.fit_transform(veriler.iloc[:,-1])

cinsiyetColumn = cinsiyetColumn.reshape(-1,1)

"""
    .reshape(-1, 1) kullanmanın amacı, veriyi bir boyuta düşürmektir. Daha önce cinsiyetColumn'ı bir 1D 
dizisi olarak kodladınız, yani bu dizi yalnızca bir sütun içeriyordu. Ancak OneHotEncoder kullanırken
bu sütunu tek bir örnek olarak kabul eder.

    Bu nedenle, OneHotEncoder'a giriş olarak bir sütun (2D) yerine bir sütun vektörü (1D) vermek gerekiyor.
Bu nedenle, .reshape(-1, 1) kullanarak, mevcut 1D diziyi 2D bir diziye dönüştürdünüz. -1 kullanarak, numpy'ın 
otomatik olarak uygun boyutu hesaplamasına izin verirsiniz ve 1 ile sadece bir sütun olduğunu belirtirsiniz.

    Özetle, .reshape(-1, 1) kullanarak, veriyi OneHotEncoder için uygun bir şekle getirdiniz ve böylece dönüşümü
başarıyla uyguladınız. Bu, OneHotEncoder'ın her bir sınıfı ayrı bir sütun olarak ele almasına olanak tanır.

"""

cinsiyetColumn = ohe.fit_transform(cinsiyetColumn).toarray()


cinsiyetDf = pd.DataFrame(data=cinsiyetColumn[:,:1], index=range(22),columns=["cinsiyet"])

finalDF = pd.concat((sonuc, sonuc2, cinsiyetDf), axis=1)



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(finalDF.drop(["boy"],axis=1), finalDF.iloc[:,3], test_size=0.33, random_state=0)



from sklearn.linear_model import LinearRegression


regressor = LinearRegression()

regressor.fit(x_train, y_train)

y_prediction = regressor.predict(x_test)




