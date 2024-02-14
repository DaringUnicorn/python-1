# Gerekli kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasından verileri okuyoruz
data = pd.read_csv("maaslar.csv")

# Bağımsız değişken olarak sadece "Eğitim Seviyesi" sütununu alıyoruz
x = data.iloc[:,1:2]

# Bağımlı değişken olarak sadece "Maaş" sütununu alıyoruz
y = data.iloc[:,2:3]

# Pandas DataFrame'lerini numpy dizilerine dönüştürüyoruz
X = x.values
Y = y.values

# Karar ağacı regresyon modelini oluşturuyoruz
from sklearn.tree import DecisionTreeRegressor
regressorDecisionTree = DecisionTreeRegressor(random_state=0)

# Modeli eğitiyoruz
regressorDecisionTree.fit(X, Y)

# Gerçek ve tahmin edilen değerler arasındaki ilişkiyi göstermek için scatter plot çizdiriyoruz
plt.scatter(X, Y, color="red")
plt.plot(X, regressorDecisionTree.predict(X))
plt.show()

# Belirli değerler için tahminler yaparak çıktıları görüntülüyoruz
print(regressorDecisionTree.predict([[11]]))
print(regressorDecisionTree.predict([[6.6]]))

# Daha doğrusal bir grafik çizmek için eğitim verilerinin üzerine bir miktar ekleme ve çıkarma yapıyoruz
P = X + 0.5
R = X - 0.5

# Tahminleri kullanarak doğrusal grafikler çizdiriyoruz
plt.plot(x, regressorDecisionTree.predict(P), color="green")
plt.plot(x, regressorDecisionTree.predict(R), color="yellow")
plt.show()

# Modelin performansını değerlendirme
from sklearn.metrics import r2_score
print(r2_score(Y, regressorDecisionTree.predict(X)))
