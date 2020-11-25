import random, sys

min = 1
max = 10

number_to_guess = random.randint(min, max)

print(number_to_guess)

guess = int(input(f'Guess the number from {min} to {max - 1}: '))

while guess != number_to_guess:
    if guess < min or guess > max:
        print(f'Choose a number from {min} to {max - 1}.')
    guess = int(input(f'Guess the number from {min} to {max - 1}: '))

print('Yay! You got that right!')
