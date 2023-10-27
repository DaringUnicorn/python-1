import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import load_model




dataFrame = pd.read_excel("C:/Users/Ayhan/Desktop/tf/merc.xlsx")
dataFrame.drop(columns="transmission", inplace=True)

print(dataFrame.describe().to_string())

print(dataFrame.isnull().sum())


# plt.figure(figsize=(7,5))
# sns.distplot(dataFrame["price"])
# plt.show()

print(dataFrame.describe().to_string())

print(dataFrame.corr()["price"].sort_values())

# sns.scatterplot(data=dataFrame, x="mileage",y="price")
# plt.show()

print(dataFrame.sort_values("price", ascending=False).head(20))

omit = int(len(dataFrame) * 0.01)
print(dataFrame.sort_values("price", ascending=False).iloc[omit:])
dataFrame = dataFrame.sort_values("price", ascending=False).iloc[omit:]
# plt.figure(figsize=(8,8))
# sns.distplot(dataFrame["price"])
# plt.show()


print(dataFrame.groupby("year").mean()["price"])


print(dataFrame[dataFrame.year != 1970].groupby("year").mean()["price"])



x = dataFrame.drop(columns=["price"]).values
y = dataFrame["price"].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)


scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = Sequential()

model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")

model.fit(x=x_train, y= y_train, validation_data=(x_test, y_test), batch_size=250, epochs=300)

lossData = pd.DataFrame(model.history.history)

# lossData.plot()

# plt.show()


predictionArray = model.predict(x_test)

mae = mean_absolute_error(y_test, predictionArray)
mse = mean_squared_error(y_test, predictionArray)

plt.scatter(y_test, predictionArray)
plt.plot(y_test, y_test, "g-*")

plt.show()


dataFrame.iloc[2]

newCarSeries = dataFrame.drop("price", axis=1).iloc[2]

newCarSeries = scaler.transform(newCarSeries.values.reshape(-1,5))

print(model.predict(newCarSeries))