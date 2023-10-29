# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#veri yükleme
dataFrame = pd.read_csv("C:/Users/Panda/OneDrive/Masaüstü/desktop/python - Kopya/machineLearning/Bölüm 3/maaslar.csv")


x = dataFrame[["Egitim Seviyesi"]]
y = dataFrame[["maas"]]

X = x.values
Y = y.values


#linear regression
#burada aslında lineer olmayan verileri lineer modele öğreterek nasıl bir sonuç elde edicez ona bakıyoruz
from sklearn.linear_model import LinearRegression

linearRegression = LinearRegression()

linearRegression.fit(X, Y)

plt.scatter(X, Y, color = "red")

plt.plot(x,linearRegression.predict(X),color="green")


#polynomial regression
#lineer olmayan model oluşturuyoruz burada

from sklearn.preprocessing import PolynomialFeatures

polynomialRegression = PolynomialFeatures(degree=4)

#lineer haldeki x verilerini polinomal hale getiriyoruz
x_polynomial = polynomialRegression.fit_transform(X)
#burada yeni bir lineer model oluşturup polinomal regresyona hazır hale getirdiğimiz verileri lineer regresyon modeli üzerinde test ediyoruz
linearRegression2 = LinearRegression()

linearRegression2.fit(x_polynomial, y)
plt.scatter(X,Y,color="blue")


#bu satırda lineer regresyon modeliyle prediction yap ama featureleri polinomal regresyon dünyasına dönüştürüp yap

plt.plot(x,linearRegression2.predict(polynomialRegression.fit_transform(X)),color="green")



print(linearRegression.predict([[11]]))
print(linearRegression.predict([[6.6]]))


#polynomial versiyona uygun hale getirilen veriyi lineer regresyon modeline verdik burada
print(linearRegression2.predict(polynomialRegression.fit_transform([[11]])))
print(linearRegression2.predict(polynomialRegression.fit_transform([[6.6]])))


# verilerin ölçeklenmesi
from sklearn.preprocessing import StandardScaler

scaler1 = StandardScaler()

xScaled = scaler1.fit_transform(X)

scaler2 = StandardScaler()

yScaled = scaler2.fit_transform(Y)


from sklearn.svm import SVR

svrRegression = SVR(kernel="rbf")

svrRegression.fit(xScaled,yScaled)

plt.scatter(xScaled,yScaled,color="red")
plt.plot(xScaled,svrRegression.predict(xScaled),color="blue")

plt.show()










