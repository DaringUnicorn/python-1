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


print(svrRegression.predict([[6.6]]))
print(svrRegression.predict([[11]]))

