import random

secret_number = random.randint(1, 20)
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess the number between 1 and 20: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number!")
        print("You got it in", attempts, "attempts.")