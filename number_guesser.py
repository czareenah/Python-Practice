# Create a number guessing game where our code will pick a random number between 1 - 100 and the user will try to guess the number

# Requirement 1: Each guess should prompt a clue whether the number in question is higher or lower or if it is right

# Requirement 2: Show how many guesses it took the user to guess the number

# Requirement 3: Add a pause after each interaction to provide a more realistic effect

import random
import time

username = input('What is your name?: ')
print(f"Hello {username}, welcome to the guessing game! I'm thinking of a number between 1 and 100.")
time.sleep(2)
print("Picking a number...")
time.sleep(3)

guess = int(input("What's your guess?: "))
correct_number = random.randint(1,100)
guess_count = 0 

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong. You need to go higher. What is your guess?: "))
    else:
        guess = int(input("Wrong. You need to go lower. What is your guess?: "))

print(f"Congrats! The right answer was {correct_number} It took you {guess_count} guesses")
