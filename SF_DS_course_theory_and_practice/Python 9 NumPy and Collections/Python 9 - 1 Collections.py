
# Counter #######################################################################
from collections import Counter

from numpy import mean

c = Counter()

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']

for car in cars:
    c[car] += 1
print(c)

c = Counter(cars)
print(c)
print(c['yellow'])
print(sum(c.values()))
print(list(c.values()))
print('\n')

cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

print(counter_moscow)
print(counter_spb)
print(counter_moscow+counter_spb)
print(counter_moscow-counter_spb)
counter_moscow.subtract(counter_spb)
print(counter_moscow)

counter_moscow = Counter(cars_moscow)
print(*counter_moscow.elements())
print(list(counter_moscow))
print(dict(counter_moscow))
print(counter_moscow.most_common())
print(counter_moscow.most_common(2))

#DefaultDict ##################################################################

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
groups = dict()

for student, group in students:
    if group not in groups:
        groups[group] = list()
    groups[group].append(student)

print(groups)

from collections import defaultdict
groups = defaultdict(list)

for student, group in students:
    groups[group].append(student)
 
print(groups)
print(groups[3])
print(groups[2021])
print(groups)

# deque

from collections import deque
dq = deque()
print(dq)
dq.append(1)
dq.append(2)
dq.append(3)
dq.appendleft(4)
dq.appendleft(5)
dq.appendleft(6)
print(dq)
dq.pop()
dq.pop()
print(dq)
dq.popleft()
x = dq.popleft()
print(dq, x)


shop = deque([1, 2, 3, 4, 5])
print(shop)
shop.extend([11, 12, 13, 14, 15, 16, 17])
print(shop)
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)

limited = deque(maxlen=3)
limited.extend([1,2,3])
print(limited)
limited.append(8)
print(limited)

temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]
days = deque(maxlen=7)
for temp in temps:
    days.append(temp)
    if len(days) == days.maxlen:
        print(round(mean(days),2), end='; ')
        
dq = deque([1,2,3,4,5])
print(dq)
dq.reverse()
print(dq)

dq = deque([1,2,3,4,5])
print(dq)
dq.rotate(2)
print(dq)
dq.rotate(-2)
print(dq)

dq = [1,2,4,2,3,1,5,4,4,4,4,4,3]
print(dq.index(4))
print(dq.count(4))