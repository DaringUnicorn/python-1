import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("maaslar_yeni.csv")


x = dataFrame.iloc[:,2:].values

y = dataFrame.iloc[:,-1].values

from sklearn.preprocessing import MinMaxScaler, StandardScaler


minMaxScaler = MinMaxScaler()
standardScaler = StandardScaler()

xMinMax = x
yMinMax = np.reshape(y, (30,1))

xStandard = standardScaler.fit_transform(x)
yStandard = standardScaler.fit_transform(np.reshape(y, (30,1)))


from sklearn.model_selection import train_test_split

x_trainMM, x_testMM, y_trainMM, y_testMM = train_test_split(xMinMax, yMinMax, test_size=0.33, random_state=0)

x_trainSS, x_testSS, y_trainSS, y_testSS = train_test_split(xStandard, yStandard, test_size=0.33, random_state=0)


#Linear regression with minMaxScaler

from sklearn.linear_model import LinearRegression

linearRegressorMM = LinearRegression()

linearRegressorMM.fit(x_trainMM, y_trainMM)

yPredictionMM = linearRegressorMM.predict(x_testMM)

plt.scatter(x,y,color="blue")
plt.plot(x, yPredictionMM,color="green")
plt.show()