# Gerekli kütüphaneleri yüklüyoruz
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

# Verileri yüklüyoruz
veriler = pd.read_csv('maaslar.csv')

# Bağımsız değişkenler (x) ve bağımlı değişken (y) olarak verileri seçiyoruz
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:3]
X = x.values
Y = y.values

# Linear Regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

# Verileri scatter plot ile görselleştiriyoruz
plt.scatter(X,Y,color='red')
plt.plot(x,lin_reg.predict(X), color = 'blue')
plt.show()

# Linear Regression R2 değeri hesaplanıyor
print('Linear R2 degeri')
print(r2_score(Y, lin_reg.predict(X)))

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures

# Degree = 2 için Polynomial Regression
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

# Verileri scatter plot ile görselleştiriyoruz
plt.scatter(X,Y,color='red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

# Degree = 4 için Polynomial Regression
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

# Verileri scatter plot ile görselleştiriyoruz
plt.scatter(X,Y,color='red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

# Polynomial Regression R2 değeri hesaplanıyor
print('Polynomial R2 degeri')
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))

# Verilerin ölçeklendirilmesi
from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(X)

sc2 = StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))

# Support Vector Regression (SVR)
from sklearn.svm import SVR
svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_olcekli, y_olcekli)

# Verileri scatter plot ile görselleştiriyoruz
plt.scatter(x_olcekli, y_olcekli, color='red')
plt.plot(x_olcekli, svr_reg.predict(x_olcekli), color='blue')
plt.show()

# SVR R2 değeri hesaplanıyor
print('SVR R2 degeri')
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)))

# Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X, Y)

# Verileri scatter plot ile görselleştiriyoruz
plt.scatter(X, Y, color='red')
plt.plot(X, r_dt.predict(X), color='blue')
plt.show()

# Decision Tree Regression R2 değeri hesaplanıyor
print('Decision Tree R2 degeri')
print(r2_score(Y, r_dt.predict(X)))

# Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=10, random_state=0)
rf_reg.fit(X, Y.ravel())

# Verileri scatter plot ile görselleştiriyoruz
plt.scatter(X, Y, color='red')
plt.plot(X, rf_reg.predict(X), color='blue')
plt.show()

# Random Forest Regression R2 değeri hesaplanıyor
print('Random Forest R2 degeri')
print(r2_score(Y, rf_reg.predict(X)))

# R2 değerlerinin özeti
print('-----------------------')
print('Linear R2 degeri')
print(r2_score(Y, lin_reg.predict(X)))

print('Polynomial R2 degeri')
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))

print('SVR R2 degeri')
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)))

print('Decision Tree R2 degeri')
print(r2_score(Y, r_dt.predict(X)))

print('Random Forest R2 degeri')
print(r2_score(Y, rf_reg.predict(X)))
