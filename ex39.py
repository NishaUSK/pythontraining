import random
number = random.randint(1, 15)
number_of_guesses = 0
while number_of_guesses < 3:
    print('Guess a number between 1 and 15:')
    guess = input()
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1
    if guess == number:
        break
