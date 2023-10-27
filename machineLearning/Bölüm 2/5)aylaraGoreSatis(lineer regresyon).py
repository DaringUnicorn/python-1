import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#verinin çağırılması
veriler = pd.read_csv("Bölüm 2/aylaraGoreSatis.csv")


sns.scatterplot(data=veriler,x="Aylar",y="Satislar")

print(veriler)

#feature ve labell olarak ayrılmaıs
aylar = veriler[["Aylar"]]

satislar = veriler[["Satislar"]]

aylarWithIloc = veriler.iloc[:,0].values
print(aylarWithIloc)

satislarWithIloc = veriler.iloc[:,1].values 

print(satislarWithIloc)

#train-test olarak ikiye ayrılması
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(aylar, satislar, test_size=0.33, random_state=0)

"""
#scaling ile belirli bir aralığa indirgenmesi
from sklearn.preprocessing import StandardScaler

standardScaler = StandardScaler()


X_train = standardScaler.fit_transform(x_train)

X_test = standardScaler.fit_transform(x_test)

Y_train = standardScaler.fit_transform(y_train)

Y_test= standardScaler.fit_transform(y_test)

"""

#train verilerini modele vererek öğrenmesini sağlama
from sklearn.linear_model import LinearRegression

linearRegression = LinearRegression()

#linearRegression.fit(X_train,Y_train)
linearRegression.fit(x_train,y_train)


#verdiğimiz verilere öğrenen modeli test verileriyle deniyoruz


#tahmin = linearRegression.predict(X_test)


tahmin = linearRegression.predict(x_test)


x_train = x_train.sort_index()

y_train = y_train.sort_index()

plt.plot(x_train,y_train)
plt.plot(x_test,tahmin)

plt.title("aylara göre satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")







































