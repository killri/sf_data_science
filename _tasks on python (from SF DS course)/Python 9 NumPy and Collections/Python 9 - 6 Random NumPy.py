# float generation
import numpy as np
print(np.random.rand()) # generated random float from (0,1)
print(np.random.rand()*100+10) # generated random float from (10,110)
print(np.random.rand(5)) # generated random float array from (0,1)
print(np.random.rand(4,4)*10+10) # generated random float array shape (4,4) or any other from (10,20)

# rand recieves *args not a (,) stucture
shape = (3, 4)
print(np.random.rand(*shape))

# sample reciever a (,) structure and does the same as rand:
shape = (2, 3)
print(np.random.sample(shape))
# uniform genetated a float un an interval
print(np.random.uniform()) # the same as rand or sample
print(np.random.uniform(-30, 50)) # random float from -30 to 50
print(np.random.uniform(0.5, 0.75, size=5)) # random 1 dim array from 0.5 to 0.75
print(np.random.uniform(-1000, 500, size=(2, 3))) # random array shape (2,3) from -1000 to 500

# int generation^ randint(low, high=None, size=None, dtype=int)
print(np.random.randint(4)) #int from [0,3]
print(np.random.randint(4, size=(2,3))) #int from [0,3]
print(np.random.randint(6, 12, size=(3,3))) # int form [6,11]

# random shuffling
arr = np.arange(6)
print(arr)
np.random.shuffle(arr) #returns None. Changes the array
print(arr)
playlist = ["The Beatles", "Pink Floyd", "ACDC", "Deep Purple"]
shuffled = np.random.permutation(playlist) # returns the shuffled array. Doesn't change the first array
print(shuffled)
print(playlist)

print(np.random.permutation(10)) # returns an array ints 0 to 9 shuffled

# random choosing: choice(a, size=None, replace=True) : 
    #a — массив или число для генерации arange(a);
    #size — желаемая форма массива (число для получения 
    # одномерного массива, кортеж — для многомерного; если параметр не задан, возвращается один объект);
    # replace — параметр, задающий, могут ли элементы повторяться (по умолчанию могут).

workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate','Ivan1', 'Nikita1', 'Maria1', 'John1', 'Kate1']
 
choice = np.random.choice(workers, size=(2,2,2), replace=False)
print(choice)

choice = np.random.choice([1,2,3,4,5,6], size=10)
print(choice) # 10 раз кубик бросили и записали в массив результат

#seed: np.random.seed(<np.uint32>).
np.random.seed(23)
print(np.random.randint(10, size=(3,4)))
print(np.random.randint(10, size=(3,4)))
print(np.random.randint(10, size=(3,4)))

