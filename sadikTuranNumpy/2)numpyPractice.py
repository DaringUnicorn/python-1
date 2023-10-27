import numpy as np

# numpy arrayi oluşturuyoruz

result = np.array([1,3,5,7,9])
print(f"elemanlarını elimizle yazdığımız numpy arrayi : {result}")


# numpy arrayini bütün elemanlarını kendimiz yazmadan aralık tanımlayarak oluşturuyoruz.
result = np.arange(1,10)
print(f"aralık vererek oluşturduğumuz numpy arrayi : {result}")

# step atayarak oluşturduğumuz numpy arrayi

result = np.arange(10,100,3)
print(f"aralık verip adım atayarak oluşturduğumuz numpy arrayi (son değer dahil değil) : {result.shape}")

# sıfırlardan oluşan bir matrix oluşturalım

result = np.zeros(10)
print(f"sıfırlardan oluşan bir boyutlu bir array : \n{result}")

result = np.zeros((5,5))
print(f"sıfırlardan oluşan 5x5 bir array : \n{result}")

result = np.ones((5,5))
print(f"birlerden oluşan 5x5 bir array : \n{result}")


# belli bi aralık verip o aralığın istenilen değerdeki eş parçaya bölünmesi

result = np.linspace(0,100,5)
print(f"0 - 100 aralığının 5 eş parçaya ayrılmış hali : \n{result}")

# verilen aralık arasında herhangi bir integer değer döndürmek

result = np.random.randint(0,10)
result = np.random.randint(10) # üst satırlar aynı şey

print(f"0,10 arasındaki (10 dahil değil) rastgele bir integer değer : \n{result}")


result = np.random.randint(0,10,3)

print(f"0,10 arasındaki (10 dahil değil) rastgele 3 integer değer : \n{result}")


# 0-1 arasında istediğimiz adette sayı üretmek

result = np.random.rand(5)

print(f"[0,1) arasından rastgele 5 değer : \n{result}")

# arange ile ürettiğimiz dizinin shapeini değiştirmek

result = np.arange(50)
print(f"bir boyutlu dizi : \n{result}")

result = result.reshape(5,10)
print(f"5x10 luk  dizi : \n{result}")


print(f"5x10 luk dizideki satırların toplamı : \n{result.sum(axis=1)}")
print(f"5x10 luk dizideki sütunların toplamı : \n{result.sum(axis=0)}")


result = np.random.randint(1,100,10)
print(f"[1,100) arasındaki üretilen 10 değer : \n{result} \nen büyüğü : \n{result.max()}\nen büyük sayının index numarası : {result.argmax()}")
print(f"[1,100) arasındaki üretilen 10 değer : \n{result} \nen küçüğü : \n{result.min()}\nen küçük sayının index numarası : {result.argmin()}")
print(f"[1,100) arasındaki üretilen 10 değer : \n{result} \n ortalaması : \n{result.mean()}")
