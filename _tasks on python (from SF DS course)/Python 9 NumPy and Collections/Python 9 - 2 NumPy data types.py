import numpy as np

a = np.int8(25)  #int8 - значит мы выделяем 8 бит под хранение типа int. Как я понял это первые 2^7 натуральных и обратные к ним. (Правда без какого-то одного элемента, видимо на границе)
print(a)

print(type(a))
print(np.iinfo(np.int8)) # iinfo выдает из расчетов параметры это типа данных. Ну и я получил ответ на вопрос какой элемент не включен в int8: 128

b = np.uint8(124) #u = unsigned. Видимо только положительные и тогда от 0 до 255 т.к. int8  дает 2^8 чисел
print(type(b))
print(np.iinfo(np.uint8))

a = np.int32(1000) 
print(a)
print(type(a))
print(np.iinfo(np.int32))

a = 2056 #перезаписали переменную и тип данных стал обычным int. Для сохранения типов надо было снова писать np.int32(2056)
print(a)
print(type(a))

a = np.int32(1000) #при операциях по умолчанию происходит приведение к типу данных, который забирает больше места
b = np.int8(8) 
c = a + b
print(c)
print(type(c))


a = np.int8(260)
print(a) #Мы попытались записать большее число в тип, которое его не может хранить. Ошибки не получили, но потеряли часть инфорамции о числе

print(np.finfo(np.float16))
print(np.finfo(np.float32))

# Надо помнить, что могут происходить потери инфорамции при указании слишком маленьких по битам типов
# Пример

print(np.float16(4.12))
print(np.float16(4.13))
print(np.float16(4.123))
print(np.float16(4.124))
print(np.float16(4.125))
print(np.float16(4.126))

# Теперь посмотрим на все доступные типы данных:
# print(np.sctypeDict)
print('\n','All real types with no repetitions')
print( *sorted( map(str, set(np.sctypeDict.values()) ) ) , sep = '\n')


print(np.uint8(-456))
print(np.iinfo(np.int64))
print(-2**15 )