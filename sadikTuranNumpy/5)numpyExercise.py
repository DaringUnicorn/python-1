import numpy as np

# 1-(10,15,30,45,60) değerlerine sahip bir numpy dizisi oluşturunuz

result = np.array([10,15,30,45,60])

print(f"(10,15,30,45,60) değerlerine sahip numpy arrayi : \n{result}\ntype : \n{type(result)}")

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz

result = np.arange(5,15)
print(f"(5-15) arasındaki sayılarla oluşturulmuş numpy arrayi : \n{result}")

# 3- (50,100) arasında beşer beşer artan bir numpy dizisi oluşturunuz

result = np.arange(50,100,5)

print(f"(50,100) arasında beşer beşer artan bir numpy dizisi : \n{result}")

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz

result = np.zeros(10)

print(f"10 elemanlı sıfırlardan oluşan bir dizi : \n{result}")

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz

result = np.ones(10)

print(f"10 elemanlı birlerden oluşan bir dizi : \n{result}")


# 6- (0,100) arasında eşit aralıklı 5 sayı üretin

result = np.linspace(0,100,5)

print(f"(0,100) arasında eşit aralıklı 5 sayı : \n{result}")


# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.

result = np.random.randint(10,30,5)
print(f"(10-30) arasında rastgele 5 tane tamsayı : \n{result}")


# 8- [-1 ile 1] arasında 10 adet sayı üretin.


result = np.random.randn(10)
print(f"[-1 ile 1] arasında 10 adet sayı tamsayı : \n{result}")



# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.

result = np.random.randint(10,50,15).reshape(3,5)

print(f"(3x5) boyutlarında (10-50) arasında rastgele bir matris : \n{result}")


# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?

print(f"Üretilen matrisin satır sayıları toplamı : \n{result.sum(axis=1)}")
print(f"Üretilen matrisin sütun sayıları toplamı : \n{result.sum(axis=0)}")



# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
print(f"Üretilen matrisin en büyük değeri : \n{result.max()}")
print(f"Üretilen matrisin en küçük değeri : \n{result.min()}")
print(f"Üretilen matrisin ortalama değeri : \n{result.mean()}")




# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır

print(f"Üretilen matrisin en büyük değerinin indeksi : \n{result.argmax()}")

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

result = np.arange(10,20)

print(f"(10-20) arasındaki sayıları içeren dizinin ilk 3 elemanı : \n{result[:3]}")

# 14- Üretilen dizinin elemanlarını tersten yazdırın.
print(f"Üretilen dizinin elemanlarını ters hali : \n{result[::-1]}")

result = np.random.randint(10,50,15).reshape(3,5)


# 15- Üretilen matrisin ilk satırını seçiniz.

print(f"Üretilen matris : \n{result}")

print(f"Üretilen matrisin ilk satırı : \n{result[0,:]}")


# 16- Üretilen matrisin 2. satır 3. sütundaki elemanı hangisidir ?

print(f"Üretilen matrisin 2. satır 3. sütundaki elemanı : \n{result[1,2]}")


# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.

print(f"Üretilen matrisin tüm satırlardaki ilk elemanı : \n{result[:,0]}")


# 18- Üretilen matrisin her bir elemanının karesini alınız.

print(f"Üretilen matrisin her bir elemanının karesi : \n{np.square(result)}")

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ?
# Aralığı (-50, +50) arasında yapınız.

even = result[result % 2 == 0]

even = even[even > 0]
print("üretilen matrisin pozitif çift olanları"even)