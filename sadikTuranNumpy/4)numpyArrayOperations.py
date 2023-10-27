import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(f"[10,100) aralığındaki rastgele 6 değer : \n{numbers1}")
print(f"[10,100) aralığındaki rastgele 6 değer : \n{numbers2}")


print(f"oluşturulan rastgele dizilerin elemanları toplamı : \n{numbers1 + numbers2}")

print(f"oluşturulan rastgele dizinin elemanlarının 10 fazlası : \n{numbers1 + 10}")

print(f"oluşturulan rastgele dizilerin elemanları farkı : \n{numbers1 - numbers2}")

print(f"oluşturulan rastgele dizinin elemanlarının 10 eksiği : \n{numbers1 - 10}")

print(f"oluşturulan rastgele dizilerin elemanları çarpımı : \n{numbers1 * numbers2}")

print(f"oluşturulan rastgele dizinin elemanlarının 10 katı : \n{numbers1 * 10}")

print(f"oluşturulan rastgele dizinin elemanlarının 10 a bölümü : \n{numbers1 / 10}")

print(f"oluşturulan rastgele dizinin elemanlarının sin değerleri : \n{np.sin(numbers1)}")

print(f"oluşturulan rastgele dizinin elemanlarının cos değerleri : \n{np.cos(numbers1)}")

print(f"oluşturulan rastgele dizinin elemanlarının karekök değerleri : \n{np.sqrt(numbers1)}")

print(f"oluşturulan rastgele dizinin elemanlarının logaritma değerleri : \n{np.log(numbers1)}")

print(f"oluşturulan rastgele dizinin elemanlarının 2x3 lük dizi hali : \n{numbers2.reshape(2,3)}")


multiNumbers1 = numbers1.reshape(2,3)
multiNumbers2 = numbers2.reshape(2,3)

print(f"2x3 lük numbers1 matrixi : \n{multiNumbers1}")
print(f"2x3 lük numbers2 matrixi : \n{multiNumbers2}")

print(f"oluşturulan rastgele dizilerin dikey olarak birleştirilmesi : \n{np.vstack((multiNumbers1, multiNumbers2))}")

print(f"oluşturulan rastgele dizilerin yatay olarak birleştirilmesi : \n{np.hstack((multiNumbers1, multiNumbers2))}")


# matrixlerin belli koşullara uygunluğunu kontrol etme 

result = numbers1 >= 50

print(f"numbers1 dizisinin elemanlarının 50 eşit veya büyük olanları (T/F olarak): \n{result}")


print(f"numbers1 dizisinin elemanlarının 50 eşit veya büyük olanları (elemanların kendisis olarak): \n{numbers1[result]}")


result = numbers1 % 2 == 0

print(f"numbers1 dizisinin elemanlarının 2 modunun sıfıra eşit olanları (T/F olarak): \n{result}")


print(f"numbers1 dizisinin elemanlarının 2 modunun sıfıra eşit olanları (elemanların kendisi olarak): \n{numbers1[result]}")













