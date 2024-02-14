import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("maaslar.csv")



x = data.iloc[:,1:2]

y = data.iloc[:,2:3]

X = x.values
Y = y.values

Z = X + 0.5
K = X - 0.4

from sklearn.ensemble import RandomForestRegressor

regressorRandomForest = RandomForestRegressor(n_estimators=10,random_state=0)

regressorRandomForest.fit(X,Y.ravel())
#Y.ravel() fonksiyonu Y değişkeni içerisindeki diziyi tek boyutlu bir diziye dönüştürmek için kullanılır

print(regressorRandomForest.predict([[6.5]]))


plt.scatter(X,Y,color="red")
plt.plot(X,regressorRandomForest.predict(X),color="blue")
plt.plot(X,regressorRandomForest.predict(Z),color="yellow")
plt.plot(x,regressorRandomForest.predict(K),color="green")

plt.show()




#random forest R^2 değeri
from sklearn.metrics import r2_score

print(r2_score(Y,regressorRandomForest.predict(X)))
print(r2_score(Y,regressorRandomForest.predict(Z)))
print(r2_score(Y,regressorRandomForest.predict(K)))













