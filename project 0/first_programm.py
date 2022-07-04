"""Guess number game"""

import numpy as np

number = np.random.randint(1,101) #generate a number

#attept count
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100:'))
    
    if predict_number > number:
        print('Your number must be less')
    elif predict_number < number:
        print('Your number must be bigger')
    else:
        print(f'Guessed right = {number} by {count} attempts')
        break #the end. And end the cicle