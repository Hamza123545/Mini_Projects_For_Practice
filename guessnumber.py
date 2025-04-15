# guess number gamme

import random


print("Welcome to the new mini project of Guess Number")

def gusseing_Number():
    secret_number = random.randint(1,10)

    while True:
        guess = int(input("Guess a Number between 1 to 10"))


        if guess == secret_number:
            print("congratulations you win")
            break

        elif guess < secret_number:
            print("to low, try again.")

        else: 
            print("too hight, try again.")


gusseing_Number()