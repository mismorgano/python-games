import random

name = input("Hello, what's your name\n")

print(f'Well, {name}, I am thinking of a number between 1 and 20')

number = random.randint(1, 20)

for i in range(6):
    print('Take a guess.')
    guess = int(input())

    if guess < number:
        print('Your guess is too low')
    
    if guess > number:
        print('Your guess is too high')

    if guess == number:
        print(f"Good job, {name}! You guessed my number in {i+1} guesses!")
        break

if guess != number:
    print(f'You lose, my number was {number}')