import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess= int(input(f"Guess the number between 1 and {x}"))
        if guess > random_number:
            print("Sorry. Guess  again. Too high.")
        elif guess < random_number:
            print("Sorry. Guess again. Too low")

    print(f'Yay. You guessed the number {random_number} correctly!')

guess(10)
