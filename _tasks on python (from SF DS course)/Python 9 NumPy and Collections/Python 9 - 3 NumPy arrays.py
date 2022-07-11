import numpy as np

arr = np.array([1,2,3,4,5])
print(type(arr))

nd_arr = np.array([[1,0,0],
                   [0,1,0],
                   [0,0,1]]
                  )

print(nd_arr)
print(nd_arr.dtype) #int32 default

#зададим массив с указанным типом данных
arr = np.array([0,1,2,3,4,5], dtype=np.int8)

arr[2] = 2000
print(arr) # ожидаемо записалось не то т.к. тип данных хранит до 2 в 7 минус 1
arr[2] = 125.5
print(arr) # привелось к int8 = 125
arr[2] = '12'
print(arr) # привелось к int8 = 12
# arr[2] = 'test'
# print(arr)  # приведение не сработало. Ошибка ValueError: invalid literal for int() with base 10: 'test'

#Изменим тип данных массива arr
arr = np.float64(arr)
print(arr) 

# Функции работа с массивами

arr = np.array([1,5,2,9,10], dtype=np.int8)
nd_arr = np.array( [[12, 45, 78],
                    [34, 56, 13],
                    [12, 98, 76],
                    [43, 23, 78]] , dtype = np.int16)

# Размерность ndim
print(arr.ndim)
print(nd_arr.ndim)
# Размер size
print(arr.size)
print(nd_arr.size)
# Форма shape
print(arr.shape)
print(nd_arr.shape)
# Сколько байт отведено под каждый элемент массива itemsize
print(arr.itemsize)
print(nd_arr.itemsize)

# Создаем нулевой массив. Функция zeros - на вхоже кортеж или число = форма массива
z_arr = np.zeros((5,4,3), dtype = np.float32)
print(z_arr.shape)
print(z_arr)

# Создадим массив аналогом range - функция arange
print(np.arange(5))

#Может от дробного по единице добавлять
print(np.arange(2.4, 6))

#Добавим 3им аргументов шаг
print(np.arange(2.4, 6, 0.2))

#Укажем тип данных
print(np.arange(2.4, 6, 0.2, dtype=np.float16))

#Лучше дробное заполнение получать через linspace

arr = np.linspace(1,2,10) #от одного до 2х разделено на 10 элементов
print(arr)
arr = np.linspace(1,2,10, endpoint = False) #тоже самое, но оотменяем правую границу как элемент. Кстати, все равно 10 элементов будет с массиве
print(arr)

# и с возможностью узнать шаг
arr, step = np.linspace(1,2,10, endpoint = True ,retstep = True) #от одного до 2х разделено на 10 элементов
print(arr, step)
arr, step = np.linspace(1,2,10, endpoint = False,  retstep = True) #тоже самое, но оотменяем правую границу как элемент. Кстати, все равно 10 элементов будет с массиве
print(arr, step)



print(np.finfo(np.float16))
print(np.finfo(np.float32))
print(np.finfo(np.float64))


arr = np.array([345234,876362.12,0,-1000,99999999], dtype=np.float64)
print(arr)


arr, step = np.linspace(-6,21,60, endpoint = True,  retstep = True) #тоже самое, но оотменяем правую границу как элемент. Кстати, все равно 10 элементов будет с массиве
print(arr, step)