# Gerekli kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasından verileri okuyoruz
data = pd.read_csv("maaslar.csv")

# Bağımsız değişken olarak eğitim seviyesini seçiyoruz
x = data.iloc[:, 1:2]

# Bağımlı değişken olarak maaşı seçiyoruz
y = data.iloc[:, 2:3]

# Verileri numpy dizilerine dönüştürüyoruz
X = x.values
Y = y.values

# Doğrusal regresyon modeli oluşturuyoruz ve eğitiyoruz
from sklearn.linear_model import LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(x, y)

# Doğrusal regresyon modelini görselleştiriyoruz
plt.scatter(x, y, color="red")
plt.plot(x, linearRegressor.predict(x), color="blue")

# Polinom regresyonu için PolynomialFeatures kullanarak özellikler oluşturuyoruz
from sklearn.preprocessing import PolynomialFeatures
polynomialRegressor = PolynomialFeatures(degree=4)
x_polynomial = polynomialRegressor.fit_transform(X)

# Polinom regresyon modelini oluşturuyoruz ve eğitiyoruz
linearRegression2 = LinearRegression()
linearRegression2.fit(x_polynomial, y)

# Polinom regresyon modelini görselleştiriyoruz
plt.scatter(X, Y, color="blue")
plt.plot(X, linearRegression2.predict(polynomialRegressor.fit_transform(X)), color="red")

# Verileri ölçeklendiriyoruz
from sklearn.preprocessing import StandardScaler
standardScaler1 = StandardScaler()
xScaled = standardScaler1.fit_transform(X)

standardScaler2 = StandardScaler()
yScaled = standardScaler2.fit_transform(Y)

# Destek Vektör Regresyon (SVR) modeli oluşturuyoruz ve eğitiyoruz
from sklearn.svm import SVR
regressorSVR = SVR(kernel="rbf")
regressorSVR.fit(xScaled, yScaled)

# SVR modelini görselleştiriyoruz
plt.scatter(xScaled, yScaled)
plt.plot(xScaled, regressorSVR.predict(xScaled))

# R^2 skoru ile modelin performansını değerlendiriyoruz
from sklearn.metrics import r2_score
print(r2_score(Y, regressorSVR.predict(X)))
