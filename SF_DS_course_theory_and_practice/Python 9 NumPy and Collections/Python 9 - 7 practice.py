# 10.6

def get_chess(a):
    import numpy as np
    arr = np.zeros((a,a), dtype=np.float32)
    arr[::2,1::2] = 1
    arr[1::2,::2] = 1
    return arr

print(get_chess(5))
# эталон совпадает
#10.7
def shuffle_seed(array):
    import numpy as np
    seed_list = np.random.randint(0, 2**32, size=None, dtype=np.uint32) # в coseboard так не работает. Он dtype не понимает
    np.random.seed(seed_list)
    return (np.random.permutation(array), seed_list)
# совпадает с эталоном
array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
print(shuffle_seed(array))

#10.8


import numpy as np
def min_max_dist(*vectors):
    dist_list = list()
    for vector1 in vectors:
        for vector2 in vectors:
            if vector1 is not vector2:
                dist_list.append(np.linalg.norm(vector1-vector2))

    return(min(dist_list),max(dist_list))

# в эталоне цикл по верхнему треугольнику таблицы расстояний. Что есть меньше лишних дествий:
#def min_max_dist(*vectors):
#   dists = list()
#   for i in range(len(vectors)):
#       for j in range(i + 1, len(vectors)):
#          dists.append(np.linalg.norm(vectors[i] - vectors[j]))
#  return (min(dists), max(dists))
    
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
print(min_max_dist(vec1, vec2, vec3))

#10.9
import numpy as np
def any_normal(*vectors):
    for vector1 in vectors:
        for vector2 in vectors:
            if vector1 is not vector2:
                if np.dot(vector1,vector2) == 0:
                    return True
    return False
# в эталоне цикл по верхнему треугольнику таблицы расстояний. Что есть меньше лишних дествий:
#def any_normal(*vectors):
#    for i in range(len(vectors)):
#        for j in range(i + 1, len(vectors)):
#            if np.dot(vectors[i], vectors[j]) == 0:
#                return True
#    return False
vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))

#10.10
import numpy as np
def get_loto(num):
    return np.random.randint(1,101, size=(num,5,5))
#совпадает с эталоном                             
print(get_loto(3))

#10.11
print('\n','10.11','\n')
import numpy as np
def get_unique_loto(num):
    aim_arr = np.zeros((num,5,5), dtype = np.uint8)
    value_arr = np.arange(100)+1
    for i in range(num):
        table = np.random.choice(value_arr , size=(5,5), replace=False)
        aim_arr[i,:,:] = table[:,:]
    return aim_arr
# все гораздо проще. Добавляем рандомные таблицы в список, а потом список превразаем в массив. Фейспалм.
#def get_unique_loto(num):
#    sample = np.arange(1, 101)
#    res = list()
#    for i in range(num):
#        res.append(np.random.choice(sample, replace=False, size=(5, 5)))
#    res = np.array(res)
#    return res    
    
                             
print(get_unique_loto(3))