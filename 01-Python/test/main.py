def add5(num=0):
    try:
        if isinstance(num, int):
            return num + 5
        elif int(num) == isinstance(num, int):
            return int(num) + 5
        else:
            return 'please enter a number'
    except ValueError as err:
        return err

#######################################

import random

def run_guess(guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue