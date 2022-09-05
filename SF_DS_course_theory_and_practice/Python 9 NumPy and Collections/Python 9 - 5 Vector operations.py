import numpy as np
vec1 = np.array([2, 4, 7, 2.5])
vec2 = np.array([12, 6, 3.6, 13])
print(vec1 + vec2)

#заметим, что списки так не складываются, а приписываются друг к другу
#Напимер со списками было бы так:
list1 = [2, 4, 7, 2.5]
list2 = [12, 6, 3.6, 13]
print(list1 + list2)
print([x+y for x,y in zip(list1,list2)])

#Можно и умножать поэлементно
print(vec1 * vec2)

#понятно, что векторы для этого должны быть одной длины
# а вот операции со скалярами разрешены
print(vec1**2)
print(vec2/3)

#векторы можно сравнивать поэлементно и даже сравнивать с чилом поэлементно. Результатом является булев вектор (что есть одномерный массив)
print(vec1 > vec2)
print(vec1 > 3)
# можно посчитать длину вектора по стандартной формуле корня и суммы квадратов
print(np.sqrt(np.sum(vec1**2)))
print(np.linalg.norm(vec1)) #встроенная функция норма
# ну и васстояние считается так
print(np.sqrt(np.sum(  (vec1-vec2)**2  )))
print(np.linalg.norm(  (vec1-vec2) ))

# ну и посчитаем скалрное произведение
print(np.sum(vec1*vec2))
print(np.dot(vec1,vec2))

# теперь посчитаем максимальный элеменрт, минимальный элемент и среднее элементов
print(np.min(vec1))
print(np.max(vec1))
print(np.mean(vec1))
print(np.median(vec1))
print(np.var(vec1)) #Дисперсия
print(np.std(vec1)) #(E(x^2) - (Ex)^2)^(1/2)
print(np.sqrt(np.mean(vec1**2)-np.mean(vec1)**2))



