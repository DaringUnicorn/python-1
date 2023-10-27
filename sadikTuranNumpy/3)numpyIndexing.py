import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75,85])

result = numbers[5]

print(f"numbers dizisindeki 5. index : \n{result}")

result = numbers[-1]
print(f"numbers dizisindeki en son eleman : \n{result}")


# belli bir aralıktaki değerleri yazdırmak

result = numbers[0:3]

print(f"numbers dizisindeki [0,3) indeks aralığındaki elemanlar : \n{result}")

result = numbers[3:]
print(f"numbers dizisindeki 3. elemandan dizinin sonuna kadar olan elemanlar : \n{result}")



result = numbers[3:]
print(f"numbers dizisindeki [0,3) indeks aralığndaki elemanlar : \n{result}")



result = numbers[::]
print(f"numbers dizisindeki bütün elemanlar : \n{result}")

result = numbers[::-1]
print(f"numbers dizisindeki elemanların sondan başa doğru yazımı : \n{result}")



numbers = numbers.reshape(3,3)

print(f"3x3 lük matrix : \n{numbers}")


# matrixlerin indekslerine ve elemanlarına ulaşmak

result = numbers[0]

print(f"3x3 lük matrixin 0. elemanı : \n{result}")

result = numbers[2]

print(f"3x3 lük matrixin 2. elemanı : \n{result}")


result = numbers[0,2]

print(f"3x3 lük matrixin 0. indexinin 2. indexindeki eleman (yani 1. satır 3. sütun): \n{result}")



result = numbers[2,1]

print(f"3x3 lük matrixin 2. indexinin 1. indexindeki eleman (yani 3. satır 2. sütun): \n{result}")


# birden fazla satır ve birden fazla sütun seçmek için slicing kullanmalıyız

result = numbers[:,2]

print(f"her satırın sadece 2. indexindeki eleman : \n{result}")


result = numbers[:,0:2]

print(f"her satırın [0,2) index aralığındaki elemanlar : \n{result}")

result = numbers[-1,:]

print(f"son satırın bütün sütunları elemanlar : \n{result}")


result = numbers[:2,:2]
print(f"baştan iki satırdaki ve baştan iki sütundaki elemanlar : \n{result}")

array1 = np.arange(0,10)
array2 = array1

# burada referans değerlerinin aynı olmasından dolayı array2 üzerinde yapılan değişiklik 
# array1 üzerinde de gözükecektir.