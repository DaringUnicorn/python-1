# Gerekli kütüphaneleri yüklüyoruz
import numpy as np
import pandas as pd

# CSV dosyasından verileri okuyoruz
data = pd.read_csv("veriler.csv")

# LabelEncoder ve OneHotEncoder sınıflarını kullanarak kategorik verileri işliyoruz
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# LabelEncoder: Kategorik verileri sayısal verilere dönüştürmek için kullanılır
labelEncoder = LabelEncoder()

# OneHotEncoder: LabelEncoder ile dönüştürülen sayısal verileri ikili (binary) vektörlere dönüştürmek için kullanılır
oneHotEncoder = OneHotEncoder()

# "ulke" ve "cinsiyet" sütunlarını ayrı ayrı işleyerek sayısal verilere dönüştürüyoruz
ulke = data.iloc[:,0].values  # "ulke" sütununu alıyoruz
cinsiyet = data.iloc[:,-1].values.reshape(-1,1)  # "cinsiyet" sütununu alıyoruz

# LabelEncoder ile "ulke" sütununu sayısal verilere dönüştürüyoruz
ulkeLabeled = labelEncoder.fit_transform(ulke)

# OneHotEncoder ile LabelEncoder ile dönüştürülen sayısal "ulke" verilerini ikili vektörlere dönüştürüyoruz
ulkeEncoded = oneHotEncoder.fit_transform(ulkeLabeled.reshape(-1,1)).toarray()

# "cinsiyet" sütununu da aynı işlemleri uygulayarak sayısal verilere dönüştürüyoruz
cinsiyetLabeled = labelEncoder.fit_transform(cinsiyet)
cinsiyetEncoded = oneHotEncoder.fit_transform(cinsiyetLabeled.reshape(-1,1)).toarray()

# OneHotEncoder ile dönüştürülen "ulke" verilerini DataFrame olarak saklıyoruz
ulkeDataFrame = pd.DataFrame(data = ulkeEncoded, index = range((22)), columns = ["fr","tr","us"])

# OneHotEncoder ile dönüştürülen "cinsiyet" verilerini DataFrame olarak saklıyoruz
cinsiyetDataFrame = pd.DataFrame(data = cinsiyetEncoded[:,0], index = range((22)), columns = ["erkek"])

# "ulke" ve "cinsiyet" sütunlarını veri kümesinden çıkarıyoruz
data.drop(["ulke", "cinsiyet"], axis = 1, inplace = True)

# DataFrame'leri veri kümesine ekliyoruz
data = pd.concat([data, ulkeDataFrame, cinsiyetDataFrame],axis=1)

# Veri setini eğitim ve test verilerine böleriz
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data.drop(["erkek"],axis=1), data["erkek"], random_state=0, test_size=0.33)

# Verileri standartlaştırırız
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train = standardScaler.fit_transform(x_train)
X_test = standardScaler.fit_transform(x_test)

# Çoklu doğrusal regresyon modelini oluşturur ve eğitiriz
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Modeli kullanarak tahminler yaparız
y_predict = regressor.predict(X_test)

# R^2 skoru ile modelin performansını değerlendiririz
from sklearn.metrics import r2_score
print(r2_score(y_test,y_predict))
