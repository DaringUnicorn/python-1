# Gerekli kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasından verileri okuyoruz
data = pd.read_csv("maaslar.csv")

# Verileri bağımlı ve bağımsız değişkenlere ayırıyoruz
x = data.iloc[:, 1:2]  # Bağımsız değişkenleri alıyoruz
y = data.iloc[:, 2:3]  # Bağımlı değişkenleri alıyoruz

X = x.values  # Bağımsız değişkenleri numpy dizisine dönüştürüyoruz
Y = y.values  # Bağımlı değişkenleri numpy dizisine dönüştürüyoruz

# Decision Tree Regressor modelini kullanarak modelimizi oluşturuyoruz ve eğitiyoruz
from sklearn.tree import DecisionTreeRegressor
regressorDecisionTree = DecisionTreeRegressor(random_state=0)
regressorDecisionTree.fit(X, Y)

# Verileri ve modelin tahminini görselleştiriyoruz
plt.scatter(X, Y, color="red")  # Verileri scatter plot ile gösteriyoruz
plt.plot(X, regressorDecisionTree.predict(X))  # Modelin tahminini çiziyoruz
plt.show()

# Belirli değerler için tahminler yapıyoruz
print(regressorDecisionTree.predict([[11]]))  # 11 değeri için tahmin
print(regressorDecisionTree.predict([[6.6]]))  # 6.6 değeri için tahmin

# Belirli bir aralıkta tahminleri çizdiriyoruz
P = X + 0.5
R = X - 0.5

plt.plot(x, regressorDecisionTree.predict(P), color="green")
plt.plot(x, regressorDecisionTree.predict(R), color="yellow")
plt.show()

# R^2 skoru ile modelin performansını değerlendiriyoruz
from sklearn.metrics import r2_score
print(r2_score(Y, regressorDecisionTree.predict(X)))
