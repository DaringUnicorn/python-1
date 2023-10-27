import numpy as np


# python list
pythonList = [1,2,3,4,5,6,7,8,9]
""" 
    genel olarak python lisetelerinin sahip olmadığı fonksiyonları kullanarak
listeler üzerinde daha üst düzey işler yapmamıza olanak sağlar.

    pythondaki normalde olan liste kavramı numpy üzerinde array kavramına
denk geliyor.


 """

# numpy array

numpyArray = np.array([1,2,3,4,5,6,7,8,9])

print(f"python listesi : {pythonList}\npython listesinin tipi : {type(pythonList)}")


print(f"numpy arrayi : {numpyArray}\nnumpy arrayin tipi : {type(numpyArray)}")


# çok boyutlu numpy dizisi

multiD = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(f"çok boyutlu numpy arrayi : \n{multiD}\n çok boyutlu numpy arrayin tipi : {type(multiD)}")


# numpy dizisinin boyutunu değiştirme

reshapedArray = numpyArray.reshape(3,3)

print(f"reshaped numpy array : \n{reshapedArray}\n the type of reshaped numpy array : {type(reshapedArray)}\nthe shape of the reshaped array : {reshapedArray.shape}\n dimension : {reshapedArray.ndim}")

