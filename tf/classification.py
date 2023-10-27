import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.models import Sequential
from keras.models import 
from keras.layers import Dense, Activation, Dropout
from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix



dataFrame = pd.read_excel("C:/Users/Ayhan/Desktop/tf/maliciousornot.xlsx")

print(dataFrame.info)
print(dataFrame.describe())
print(dataFrame.corr()["Type"].sort_values())

# dataFrame.corr()["Type"].sort_values().plot(kind="bar")
# plt.show()

y = dataFrame["Type"].values
x = dataFrame.drop("Type", axis=1).values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.3, random_state= 15)

scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = Sequential()

model.add(Dense(units=30, activation="relu"))
model.add(Dropout(rate=0.6))

model.add(Dense(units=15, activation="relu"))
model.add(Dropout(rate=0.6))

model.add(Dense(units=15, activation="relu"))
model.add(Dropout(rate=0.6))

model.add(Dense(units=1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam")

earlyStopping = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=25)


# model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test, y_test), verbose=1)
model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test, y_test), verbose=1, callbacks=[earlyStopping])


modelLoss = pd.DataFrame(model.history.history) 
modelLoss.plot()
plt.show()


predictions = model.predict_step(x_test)
print(classification_report(y_test,predictions))