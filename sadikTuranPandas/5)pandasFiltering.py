import pandas as pd
import numpy as np


data = np.random.randint(10,100,75).reshape(15,5)

print(data)

df = pd.DataFrame(data=data, columns=["Column1","Column2","Column3","Column4","Column5"])

result = df
print(df)

# dataframe içerisinde bulunan column bilgisini almak

print(f"dataframedeki column isimleri : \n{df.columns}")

# dataframe üzerindeki ilk 5 kaydı ya da ilk kaç tanesi isteniyorsa o kadarını çağırmak

print(f"dataframedeki ilk 5 kayıt : \n{df.head()}")

print(f"dataframedeki ilk 7 kayıt : \n{df.head(7)}")


# dataframe üzerindeki son 5 kaydı ya da son kaç tanesi isteniyorsa o kadarını çağırmak

print(f"dataframedeki son 5 kayıt : \n{df.tail()}")

print(f"dataframedeki son 7 kayıt : \n{df.tail(7)}")


# dataframe üzerindeki baştan ya da sondan veri getirirken sadece istenilen kolondan veri getirilmesi

print(f"dataframedeki Column1 sütununun ilk 5 kaydı : \n{df["Column1"].head()}")


# birden fazla column seçimi yapmak istersek de liste içerisinde o columnları göndermem yeterli

print(f"dataframede birden fazla column seçimi : \n{df[[ "Column1" , "Column2" ]].head()}")

print(f"dataframede satır aralığı vererek birden fazla column seçimi : \n{df[5: 15][["Column1" , "Column2"]].head()}")


print(f"mantıksal operatör kullanarak dataframe üzerinde operasyon gerçekleştirme : \n{df > 50}")

print(f"mantıksal operatör kullanarak dataframe üzerinde operasyon gerçekleştirme ve değerleri görme : \n{df[df > 50]}")

print(f"mantıksal operatör kullanarak dataframe üzerinde operasyon gerçekleştirme (istenilen columndaki değerler için): \n{df["Column1"] > 50}")

print(f"mantıksal operatör kullanarak dataframe üzerinde operasyon gerçekleştirme ve değerleri görme(istenilen columndaki değerler için): \n{df[df["Column1"] > 50]}")


# yukarıdaki satırda değerler bütün columnları barındıracak şekilde dönüyordu alttakinde ise sadece
#istenilen columnları geri döndürüyor
print(f"mantıksal operatör kullanarak dataframe üzerinde operasyon gerçekleştirme ve değerleri görme(istenilen columndaki değerler için): \n{df[df["Column1"] > 50][["Column1", "Column2"]]}")

# birden fazla koşul ile veri çağırma
print(f"mantıksal operatörler ile koşul birden fazla koşul kullanarak veri çağırma : \n{df[(df["Column1"] >50) & (df["Column1"] <= 70)]}")

print(f"mantıksal operatörler ile koşul birden fazla koşul kullanarak veri çağırma (column aralığı vererek) : \n{df[(df["Column1"] >50) & (df["Column1"] <= 70)][["Column1", "Column2"]]}")


# 

print(f"Column1 >= 50 & Column1 %2 == 0 koşulunun df.query() metodu ile gerçekleştirilmesi : \n{df.query("Column1 >= 50 & Column1 %2 == 0")}")