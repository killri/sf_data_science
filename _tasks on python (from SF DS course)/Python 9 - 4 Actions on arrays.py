import numpy as np
arr = np.arange(8)
print(arr)

# Изменим shape
arr.shape = (2,4)
print(arr)

# Теперь сделаем тоже самое, но не изменяя исходный массив, а сохраняя данные в новый
arr = np.arange(8)
arr_new = arr.reshape((2,4))
print(arr_new)
# Атрибур order функции reshape
arr = np.arange(8)
arr_new = arr.reshape((2,4), order='F') 
print(arr_new)

#Транспортруем массив функцией transpose. Одномерный массив не транспонируется
arr = np.arange(8)
arr.shape = (2,4)
print (arr)
print(arr.transpose())