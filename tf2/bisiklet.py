import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense




bisikletFiyatlari = pd.read_excel("bisiklet_fiyatlari.xlsx")

# sb.pairplot(bisikletFiyatlari) 
""" 
    üst satırdaki kod veri setindeki featurların birbirlerine göre
olan durumlarını gösterir.
    
"""

# plt.show()

fiyatSeri = bisikletFiyatlari["Fiyat"]
fiyatDizi = bisikletFiyatlari["Fiyat"].values


print("fiyatSeri type : ",type(fiyatSeri))

print("fiyatDizi type : ",type(fiyatDizi))
""" 
    yukarıdaki ilk satır veri setinden aldığı kolonu seri şeklinde 
döndürür. ikincisi ise dizi şeklinde döndürür

"""
y = bisikletFiyatlari["Fiyat"].values
x = bisikletFiyatlari[["BisikletOzellik1", "BisikletOzellik2"]].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=15)


scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

"""
    fit_transform ile modelin öğrenebileceği bir düzeye indirgedik 
verileri

"""

model = Sequential()
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))


model.add(Dense(1))

model.compile(optimizer="rmsprop" , loss="mse")

"""
    modelin çeşidini seçip katmanlarımızı oluşturuyoruz dense ile
activation function olarak burada relu seçtik ve en sonda dabi tane 
output layer ekliyoruz.
"""

print(model.fit(x_train, y_train,epochs=170))

""" 
    modeli x_train ve y_train setleriyle eğitip epoch (bütün veriyi analiz)
değerini veriyoruz ve sonuca göre hareket ediyoruz.

"""

loss = model.history.history # loss değerlerinin listesini döndürüyor.

print(f"model history dictionary : \n{loss}")

print(f"model history loss column : \n{loss['loss']}")
# yukarıdaki satır bir dictionary döndürüyor dolayısıyla loss değişkenini kullanırken
# bunu göz önünde bulundurmalıyız

""" 
Model eğitiminde "loss" (kayıp) terimi, bir makine öğrenme veya derin öğrenme modelinin
tahminlerinin gerçek değerlerden ne kadar farklı olduğunu ölçen bir metriktir. Loss, genellikle
bir öğrenme algoritması tarafından minimize edilmeye çalışılan bir fonksiyondur. Bu fonksiyon, 
modelin ne kadar iyi veya kötü performans gösterdiğini belirlemek için kullanılır.

Loss, modelin tahmin ettiği çıktıların gerçek etiketlerden ne kadar uzak olduğunu nicel olarak
ifade eder. Bu uzaklık, farklı görevler için farklı şekillerde ölçülebilir. Örneğin, sınıflandırma
problemleri için çapraz entropi loss kullanılabilirken, regresyon problemleri için ortalama kare
hatası (MSE) kullanılabilir.

Eğitim sırasında, model genellikle loss fonksiyonunu minimize etmek için bir optimizasyon
algoritması kullanır. Bu, modelin daha iyi tahminler yapmasını ve verilere daha iyi uymasını sağlar.
Loss, modelin eğitim performansının bir göstergesi olarak kullanılır ve eğitim süreci boyunca
izlenir. İyi bir eğitilmiş model, loss değerini zaman içinde azaltır ve gerçek verilere daha iyi
uyar.

Dolayısıyla, loss, bir modelin ne kadar başarılı olduğunu değerlendirmek ve geliştirmek için önemli
bir ölçüttür.

 """

# sb.lineplot(x=range(len(loss['loss'])), y=loss['loss'])
# plt.show()

trainLoss = model.evaluate(x_train, y_train, verbose=0)

testLoss = model.evaluate(x_test, y_test, verbose=0)

# evaluate fonksiyonunu hem test hem de train için kullanıp ikisini kıyaslayarak model hakkında
# fikir elde edebiliriz


print(f"train loss : \n{trainLoss}")

print(f"test loss : \n{testLoss}")

""" 
    eğittiğimiz modelein ne kadar doğru iş yapabildiğinin ölçebilmek için için test olarak ayırdığımız
veriyi kullanarak modelden sonuç alıcaz ve bu aldığımız sonuçları da y_test verileriyle 
karşlıaştıracağız çünkü x_test özelliklerinin gerçek etiketler y_test ler idi. sonuç olarak
modelin verdiği etiket değerleri ile y_test setini kıyaslayıp ne kadar accurate olduğuna bakıcaz

 """


testPredictions = model.predict(x_test)

print(f"modelin tahmin ettiği y_test arrayi (yukarıdaki kod satırı dizi döndürüyor) : \n{testPredictions} \n type : \n{type(testPredictions)}")


predictionsDf = pd.DataFrame(y_test, columns=["Actual Y"])
print(f"tahmin dataframei : \n{predictionsDf}")

""" 
    dizi olarak döndürülen testPredictions değişkenini seri haline getirmeliyim ki dataframe
içerisine yerleştirebileyim

"""


testPredictionsSerie = pd.Series(testPredictions.reshape(330,))

print(f"tahmin serisi : \n{testPredictionsSerie}")


predictionsDf  = pd.concat([predictionsDf, testPredictionsSerie], axis=1)

predictionsDf.columns = ["Actual Y", "Predicted Y"]

print(f"modelin yaptığı tahminleri kıyaslamak için oluşturduğumuz dataframe : \n{predictionsDf}")


# sb.scatterplot(x="Actual Y", y="Predicted Y",  data= predictionsDf)
# plt.show()


""" 
    şimdiye kadar hataların ölçümünü mse ile yaptık buradan sonraki adımda da absolute error hesabı 
ile yapıcaz 

 """

from sklearn.metrics import mean_absolute_error, mean_squared_error

absoluteError = mean_absolute_error(predictionsDf["Actual Y"],predictionsDf["Predicted Y"])

meanSquaredError = mean_squared_error(predictionsDf["Actual Y"], predictionsDf["Predicted Y"])

print(f"mean absolute error : \n{absoluteError}")


print(f"mean squared error : \n{meanSquaredError}")


print(f"dataframe in özellikleri hakkında : \n{bisikletFiyatlari.describe()}")

# yeni bi bisikletin özellikleri tanımlayıp modelin onun üzerinde nasıl bir sonuç 
# çıkaracağını gözlemliycez

newBicycleFeatures = [[1760,1758]]

# şimdi modele bu verileri gönderebilmek için elimizdeki bisiklet özelliklerini scale etmemiz
# gerekiyor

scaledNewFeatures = scaler.transform(newBicycleFeatures)

newBicycleLabel = model.predict(scaledNewFeatures)




print(f"yeni verdiğimiz bisikletin özelliklerine göre modelin yaptığı label : \n{newBicycleLabel}")


from keras.models import load_model

model.save("bisiklet_modeli.keras")

calledModel = load_model("bisiklet_modeli.keras")


print(f"cağırılan model : \n{calledModel.predict(newBicycleFeatures)}") 


