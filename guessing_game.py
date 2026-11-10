import random

# Choose a secret number from 1 to 10
secret = random.randint(1, 10)

# Keep asking until the user guesses correctly
while True:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct")
        break
