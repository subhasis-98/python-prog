import random

number = random.randint(1, 10)
attempts = 0

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 10. Can you guess it?")

while True:
    print("Enter your guess: ", end="")
    player_guess = int(input())
    attempts += 1

    if player_guess > number:
        print("Too high! Try again.")
    elif player_guess < number:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
