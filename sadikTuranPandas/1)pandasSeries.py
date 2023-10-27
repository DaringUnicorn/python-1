import pandas as pd
import numpy as np

pandasSeries = pd.Series()

print(f"pandas serisi : \n{pandasSeries}\ntipi : \n{type(pandasSeries)}")

numbers = [20,30,40,50]

print(f"python listesi : \n{numbers}\ntipi : \n{type(numbers)}")

series = pd.Series(numbers)

print(f"pandas serisi : \n{series}\ntipi : \n{type(series)}")

letters = ["a","b","c","d"]

letterSeries = pd.Series(letters)

print(f"string pandas serisi : \n{letterSeries}\ntipi : \n{type(letterSeries)}")

""" 
numpydaki dizilerin içerisindeki elemanların hepsinin veri tipinin aynı olma zorunluluğu
vardır, fakat pandas serileri için aynı şey geçerli değildir.

 """


mixed = ["a","b","c","d",50]

mixedSeries = pd.Series(mixed)

print(f"karışık veri tipi olan serisi : \n{mixedSeries}\ntipi : \n{type(mixedSeries)}")


scalar = 5

scalarSeries = pd.Series(scalar)

print(f"scalar pandas serisi : \n{scalarSeries}\ntipi : \n{type(scalarSeries)}")


# aşağıdaki satır pandas serisinde kullanıcının indeksleri manuel atamasını gösteriyor

manualIndex = pd.Series(5,[0,1,2,3])

print(f"pandas serisi : \n{manualIndex}")


manualIndex = pd.Series(5,["a","b","c","d"])

print(f"pandas serisi : \n{manualIndex}")


# dictionary ile pandas serisi oluşturma

dict = {"a":10,"b":20,"c":30,"d":40}

dictSeries = pd.Series(dict)

print(f"dictionary ile oluşturulmuş pandas serisi : \n{dictSeries}")



randomNumber = np.random.randint(10,100,6)

randomSerie = pd.Series(randomNumber)


print(f"random sayılarla oluşturulmuş pandas serisi : \n{randomSerie}")


# aşağıdaki satırda ilk parametre value bilgisi diğeri de key bilgisidir
newSerie = pd.Series([20,30,40,50],["a","b","c","d"])

print(f"birinci eleman : \n{newSerie[0]}")

print(f"birinci eleman : \n{newSerie["a"]}")

print(f"son eleman : \n{newSerie[-1]}")

print(f"son eleman : \n{newSerie["d"]}")

print(f"ilk iki eleman : \n{newSerie[:2]}")

print(f"son iki eleman : \n{newSerie[-2:]}")

# ardışık olmayarak birden fazla indeks vererek eleman çağırabiliriz fakat 
#gönderdiğimiz parametre bir liste olmalı

print(f"birden fazla eleman çağırılması : \n{newSerie[["a","c"]]}")


print(f"pandas serisinin boyutu : \n{newSerie.ndim}")

print(f"pandas serisinin veri tipi : \n{newSerie.dtype}")

print(f"pandas serisinin shapei  : \n{newSerie.shape}")

print(f"pandas serisinin elemanlarının toplamı  : \n{newSerie.sum()}")

print(f"pandas serisinin en büyük elemanı : \n{newSerie.max()}")

print(f"pandas serisinin en küçük elemanı : \n{newSerie.min()}")

# pandas serisi üzerinde matematiksel ve mantıksal operasyonlar gerçekleştirilebilir


print(f"iki serinin toplamı : \n{newSerie + newSerie}")

print(f"sayı ve seri toplamı : \n{newSerie + 50}")

print(f"pandas serisinin karekökü : \n{np.sqrt(newSerie)}")

print(f"mantık operasyonu : \n{newSerie > 30}")

print(f"mantık operasyonu : \n{newSerie[newSerie > 30]}")

""" 
    iki pandas serisini toplarken her ikisinde de bulunan key değerleri denk değilse
denk olmayanlar için pandas NaN value ile doldurur karşılığı olmayan değerlerin toplam
sonuçlarını

 """
opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])


total = opel2018 + opel2019
print(f"iki seri toplamı : \n{total}")