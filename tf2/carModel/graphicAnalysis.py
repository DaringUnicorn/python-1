import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


dataframe = pd.read_excel("merc.xlsx")


# sns.displot(dataframe["price"])
# plt.show()

# sns.countplot(dataframe["year"])
# plt.show()

dataframe.drop(['transmission'],inplace=True,axis=1)


print(dataframe.corr()["price"].sort_values())

# sns.scatterplot(x="mileage",y="price",data=dataframe)

# plt.show()

print(dataframe.sort_values("price",ascending=False).head(30))

drop = int(len(dataframe) * 0.01)

cleanDataframe = dataframe.sort_values("price",ascending=False).iloc[drop:,:]

print("yeni set : \n",cleanDataframe.sort_values("price",ascending=False).head(30))

# sns.distplot(cleanDataframe["price"])
# plt.show()

print("yıllara göre araç fiyatlarının ortalaması",cleanDataframe.groupby("year").mean()["price"])


print("1970 yılı hariç arabalar",dataframe[dataframe["year"] != 1970].groupby("year").mean()["price"])


cleanDataframe = cleanDataframe[cleanDataframe["year"] != 1970]

y = cleanDataframe["price"].values
x = cleanDataframe.drop("price",axis=1).values


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=10)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.fit_transform(x_test)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))

model.add(Dense(1))


model.compile(optimizer="adam",loss="mse")


model.fit(x=x_train,  y=y_train, validation_data=(x_test,y_test),epochs=30,batch_size=250)


lossData = pd.DataFrame(model.history.history)


print(lossData)

# lossData.plot()
# plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error

tahminDizisi =model.predict(x_test)

print("tahmin \n", tahminDizisi)


print("mean absolut error : \n",mean_absolute_error(y_test,tahminDizisi))


# plt.scatter(y_test,tahminDizisi)

# plt.plot(y_test,y_test, "g-*")

# plt.show()


yeniArabaSeries = dataframe.drop("price", axis=1).iloc[2]

yeniArabaSeries = scaler.transform(yeniArabaSeries.values.reshape(-1,5))


print("yeni tahmin\n",model.predict(yeniArabaSeries))