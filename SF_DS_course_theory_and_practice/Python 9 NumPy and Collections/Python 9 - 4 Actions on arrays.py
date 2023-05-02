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

#Индексация
arr = np.linspace(1,2,6)
print(arr[2])
print(arr[2:4])
print(arr[::-1])

nd_array = np.linspace(0,6,12, endpoint=False).reshape(3,4)
print(nd_array)
print(nd_array[1][2])
print(nd_array[1,2])
print(nd_array[:2,2])
print(nd_array[1:,2:4])
print(nd_array[:,2:4])
print(nd_array[:2])

#Sorting in arrays
arr = np.array([23,12,45,12,23,4,15,3])
arr_new = np.sort(arr)
print(arr_new)
arr.sort()
print(arr)

# Пропущенные значения
data = np.array([4, 9, -4, -3])
roots = np.sqrt(data)
print(roots)
print(sum(roots))
print(np.isnan(roots))
roots[np.isnan(roots)] = 0
print(roots)