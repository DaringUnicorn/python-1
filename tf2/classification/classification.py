import pandas as pd 
import numpy as np

dataframe = pd.read_excel(r"C:\Users\Panda\OneDrive\Masaüstü\desktop\python\tf2\classification\maliciousornot.xlsx")


print(dataframe.to_string())

print(dataframe.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# sns.countplot(x="Type",data=dataframe)
# plt.show()

dataframe.corr()["Type"].sort_values().plot(kind="bar")

plt.show()


y = dataframe["Type"][:546].values

print("y",y.shape)
x = dataframe.drop(dataframe["Type"]).values
print("x",x.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=15)

from sklearn.preprocessing import MinMaxScaler


scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.fit_transform(x_test)

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.callbacks import EarlyStopping

model = Sequential()

# model.add(Dense(units=30,activation="relu"))
# model.add(Dense(units=15,activation="relu"))
# model.add(Dense(units=15,activation="relu"))
# model.add(Dense(units=1,activation="sigmoid"))


# model.compile(loss="binary_crossentropy",optimizer="adam")

# model.fit(x=x_train, y=y_train, validation_data=(x_test,y_test), epochs=700, verbose=1)


# modelKaybi = pd.DataFrame(model.history.history)

# modelKaybi.plot()
# plt.show()




model.add(Dense(units=30,activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=15,activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=15,activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=1,activation="sigmoid"))


model.compile(loss="binary_crossentropy",optimizer="adam")

earlyStopping = EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=25)

model.fit(x=x_train, y=y_train, validation_data=(x_test,y_test), epochs=700, verbose=1,callbacks=(earlyStopping))


modelKaybi = pd.DataFrame(model.history.history)

modelKaybi.plot()
plt.show()


tahminler = model.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test,tahminler))



