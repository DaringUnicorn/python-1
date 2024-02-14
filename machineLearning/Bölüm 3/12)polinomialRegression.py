# Gerekli kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasından verileri okuyoruz
data = pd.read_csv("maaslar.csv")

# Bağımsız değişken olarak 'x' ve bağımlı değişken olarak 'y' sütunlarını seçiyoruz
x = data.iloc[:,1:2]
y = data.iloc[:,2:3]

# Verileri numpy dizilerine dönüştürüyoruz
X = x.values
Y = y.values

# Doğrusal regresyon modelini oluşturup eğitiyoruz
from sklearn.linear_model import LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(x, y)

# Verileri görselleştiriyoruz
plt.scatter(x, y, color="red")
plt.plot(x, linearRegressor.predict(x), color="blue")

# Polinom regresyonu için PolynomialFeatures kullanarak 4. dereceden polinomlar oluşturuyoruz
from sklearn.preprocessing import PolynomialFeatures
polynomialRegressor = PolynomialFeatures(degree=4)
x_polynomial = polynomialRegressor.fit_transform(X)

# Polinom regresyon modelini oluşturup eğitiyoruz
linearRegression2 = LinearRegression()
linearRegression2.fit(x_polynomial, y)

# Verileri görselleştiriyoruz
plt.scatter(X, Y, color="blue")
plt.plot(X, linearRegression2.predict(polynomialRegressor.fit_transform(X)), color="red")

# Belirli bir değer için tahmin yapma
print(linearRegression2.predict(polynomialRegressor.fit_transform([[11]])))

# R^2 skorları ile modellerin performansını değerlendiriyoruz
from sklearn.metrics import r2_score
print(r2_score(Y, linearRegressor.predict(x)))
print(r2_score(Y, linearRegression2.predict(polynomialRegressor.fit_transform(X))))


# Grafikleri gösterme
plt.show()
