"""Guess number game. The computer generates and guesses itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Trying to guess the number deviding the interval where the number is by 2

    Args:
        number (int, optional): The number generated. Defaults to 1.

    Returns:
        int: Attempts count
    """
    count = 0
    interval = [0,100] 
    while True:
        count += 1
        predict_number = interval[0] + (interval[1]-interval[0])//2 #predicting the number to be the middle of the interval rounded down
        if number == predict_number:
            break
        elif number > predict_number:
            interval[0] = predict_number+1 #we don't need to start the interval with the predict_number, but we need to evoid 99 + 1//2 = 99, and number = 100 is never guessed/ That's why left border is +1 
        else:
            interval[1] = predict_number
        
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
    max_attempt = np.max(count_ls)
    print(f'Your algorithm predicts in {score} attempts on average. Max attepmt count is {max_attempt}')
    return(score)

if __name__ == '__main__':
    score_game(random_predict) 