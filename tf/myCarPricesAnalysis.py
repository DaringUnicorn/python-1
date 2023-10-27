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


dataFrame = pd.read_csv("C:/Users/Ayhan/Desktop/tf/audi.csv")

dataFrame.drop(columns=["model", "fuelType", "transmission"], axis=1, inplace=True)

print(dataFrame.describe().to_string())

# sns.pairplot(data=dataFrame)
# plt.show()

print(dataFrame.isnull().sum())

# plt.figure(figsize=(8,6))
# sns.distplot(dataFrame["price"])
# plt.show()
print(dataFrame.describe().to_string())

omit = int(len(dataFrame) * 0.01)

dataFrame = dataFrame.sort_values("price",ascending=False).iloc[omit:]
plt.figure(figsize=(8,8))
sns.distplot(dataFrame["price"])
plt.show()


x = dataFrame.drop(columns=["price"]).values
y = dataFrame["price"].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=20)


scaler = MinMaxScaler()


x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = Sequential()


model.add(Dense(units=12, activation="relu"))
model.add(Dense(units=12, activation="relu"))
model.add(Dense(units=12, activation="relu"))
model.add(Dense(units=12, activation="relu"))
model.add(Dense(units=12, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")


model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test), batch_size= 250, epochs=300)

lossData = pd.DataFrame(model.history.history)


predictionArray = model.predict(x_test)

mae = mean_absolute_error(y_test, predictionArray)
mse = mean_squared_error(y_test, predictionArray)

print(f"mae : {mae} mse : {mse}")


plt.scatter(y_test, predictionArray)

plt.show()
