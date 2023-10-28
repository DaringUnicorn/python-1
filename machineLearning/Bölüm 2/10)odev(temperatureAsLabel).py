import pandas as pd
import numpy as np

dataFrame = pd.read_csv("C:/Users/Panda/OneDrive/Masaüstü/desktop/python - Kopya/machineLearning/Bölüm 2/odevinVeriKumesi.csv")

#missingValue = dataFrame.isnull().sum()


from sklearn import preprocessing

labelEncoder = preprocessing.LabelEncoder()

#outlook = dataFrame.iloc[:,0].values
"""
    yukarıdaki kod satırını kullanarak ohe üzerinden
kategorik verileri sayısal verilere dönüştürmeye çalışınca
dataFrame üzerindeki veriler de aynı şekilde değişime uğruyor.


"""



outlook = dataFrame[["outlook"]].values
"""
    bu kod satırıyla işlem yapınca yukarıdaki yorum bloğunda
bahsettiğim durum olmuyor.

"""



outlook = outlook.reshape(-1,1)

outlook[:,0] = labelEncoder.fit_transform(outlook[:,0])

ohe = preprocessing.OneHotEncoder()

outlookOHE = ohe.fit_transform(outlook).toarray()

outlookDF = pd.DataFrame(data=outlookOHE, index= range(14), columns=["overcast","rainy","sunny"])








windy = dataFrame[["windy"]].values

windy = windy.reshape(-1,1)

windy[:,0] = labelEncoder.fit_transform(windy[:,0])

windyOHE = ohe.fit_transform(windy).toarray()

windyDF = pd.DataFrame(data=windyOHE[:,1], index=range(14), columns=["windy"])




play = dataFrame[["play"]].values

play = play.reshape(-1,1)

play[:,0] = labelEncoder.fit_transform(play[:,0])

playOHE = ohe.fit_transform(play).toarray()

playDF = pd.DataFrame(data=playOHE[:,1], index=range(14), columns=["play"])


#aşağıdaki satırda temperature label olarak seçildi ve model onu tahmin edecek
finalDF = pd.concat((outlookDF,windyDF,playDF, dataFrame[["humidity"]]),axis=1)


#aşağıdaki satır yukarıda yaptığımız bütün encoding işlemlerini tek seferde yaptı sadece binary değer olmayanları yapmak kaldı
veriler = dataFrame.apply(preprocessing.LabelEncoder().fit_transform)

kategorik = veriler[["outlook"]]
kategorik = ohe.fit_transform(kategorik).toarray()

kategorikDF = pd.DataFrame(data=kategorik, index=range(14), columns=["overcast","rainy","sunny"])

#test-train split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(finalDF, dataFrame[["temperature"]], test_size=0.33, random_state=0)









#regresyon modeli
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train, y_train)

y_prediction = regressor.predict(x_test)






#p value gözlemlemek içiçn istatistik verileri
import statsmodels.api as sm

X = np.append(arr=np.ones((14,1)).astype(int),values=finalDF,axis=1)

X_l = finalDF.iloc[:,[0,1,2,3,4,5]].values

model = sm.OLS(dataFrame[["humidity"]], X_l).fit()

print(model.summary())















