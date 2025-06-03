import random

number = random.randint(1,100)
guess = 0

while guess != number:

    guess = int(input("Guess a number :"))

    if guess < number:
        print("Guess Higher")
    elif guess > number:
        print("Guess Lower :")
    else:
        print("You Won")
        break