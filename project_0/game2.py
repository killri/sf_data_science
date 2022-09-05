"""Guess number game. The computer generates and guesses itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Trying to guess the number randomly

    Args:
        number (int, optional): The number generated. Defaults to 1.

    Returns:
        int: Attempts count
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
        
    return count

def score_game(random_predict) -> int:
    """Estimate avarage attemts of guessing a number by a function by 1000 tries

    Args:
        random_predict (_type_): guess function

    Returns:
        int: avarage attempt count
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size =(1000)) #genetated 1000 random numbers
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Your algorithm predicts mean in {score} attempts')
    return(score)

# print(f'Attempts {random_predict(10)}')
if __name__ == '__main__':
    score_game(random_predict) 