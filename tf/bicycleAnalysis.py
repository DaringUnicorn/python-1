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



dataFrame = pd.read_excel("C:/Users/Ayhan/Desktop/tf/bisiklet_fiyatlari.xlsx")

print(dataFrame)

# sns.pairplot(data=dataFrame) #veriyi featurelarına göre bi görüntüledik

# plt.show()

x = dataFrame[["BisikletOzellik1", "BisikletOzellik2"]].values
y = dataFrame["Fiyat"].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.33, random_state= 15)

scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


model = Sequential()

model.add(Dense(units=4, activation="relu"))
model.add(Dense(units=4, activation="relu"))
model.add(Dense(units=4, activation="relu"))


model.add(Dense(1))

model.compile(optimizer="rmsprop", loss="mse")

model.fit(x_train, y_train, epochs=250)

loss = model.history.history["loss"]

# sns.lineplot(x=range(len(loss)), y=loss)
# plt.show()

trainLoss = model.evaluate(x_train, y_train, verbose=0)
testLoss = model.evaluate(x_test, y_test, verbose=0)

print(f"train loss : {trainLoss}, test loss : {testLoss}")


testPredictions = model.predict(x_test)
print(testPredictions)

predictionsDataFrame = pd.DataFrame(y_test, columns=["Actual Y"])
print(predictionsDataFrame)

testPredictions = pd.Series(testPredictions.reshape(330,))

predictionsDataFrame = pd.concat([predictionsDataFrame, testPredictions], axis=1)

predictionsDataFrame.columns = ["Actual Y", "Prediction Y"]

print(predictionsDataFrame)

# sns.scatterplot(x="Prediction Y", y= "Actual Y", data=predictionsDataFrame)
# plt.show()

print("mean absolute error : ",mean_absolute_error(predictionsDataFrame["Actual Y"], predictionsDataFrame["Prediction Y"]))


print("mean squarred error : ",mean_squared_error(predictionsDataFrame["Actual Y"], predictionsDataFrame["Prediction Y"]))



print(dataFrame.describe())


yeniBisikletOzellikler = [[1750,1748]]

yeni = scaler.transform(yeniBisikletOzellikler)

print(model.predict(yeni))

model.save("bisiklet_modeli.h5")