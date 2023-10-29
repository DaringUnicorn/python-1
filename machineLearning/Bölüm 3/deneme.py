import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataFrame = pd.read_csv("C:/Users/Panda/OneDrive/Masaüstü/desktop/python - Kopya/machineLearning/Bölüm 3/maaslar.csv")

x = dataFrame[["Egitim Seviyesi"]]
y = dataFrame[["maas"]]

X = x.values
Y = y.values


#burada aslında lineer olmayan verileri lineer modele öğreterek nasıl bir sonuç elde edicez ona bakıyoruz
from sklearn.linear_model import LinearRegression

linearRegression = LinearRegression()

linearRegression.fit(X, Y)



plt.scatter(X,Y,color="red")

plt.plot(X, linearRegression.predict(X),color="blue")
plt.show()

#lineer olmayan model oluşturuyoruz burada
from sklearn.preprocessing import PolynomialFeatures

polynomialRegression = PolynomialFeatures(degree=3)

#lineer haldeki x verilerini polinomal hale getiriyoruz

xPolynomial = polynomialRegression.fit_transform(X)
print(xPolynomial)
#burada yeni bir lineer model oluşturup polinomal regresyona hazır hale getirdiğimiz verileri lineer regresyon modeli üzerinde test ediyoruz
linearRegression2 = LinearRegression()

linearRegression2.fit(xPolynomial, Y)

plt.scatter(X,Y)


#bu satırda lineer regresyon modeliyle prediction yap ama featureleri polinomal regresyon dünyasına dönüştürüp yap
plt.plot(X, linearRegression2.predict(polynomialRegression.fit_transform(X)))

plt.show()


print(linearRegression.predict([[11]]))
print(linearRegression.predict([[6.6]]))

print(linearRegression2.predict((polynomialRegression.fit_transform([[6.6]]))))
print(linearRegression2.predict((polynomialRegression.fit_transform([[11]])))) 

