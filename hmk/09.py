# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
from random import randint
number = randint(1,9)
print("guess the number...")
guess = int(input())
if guess>number:
    print("too high")
elif guess<number:
    print("too low")
else:
    print(f"you're right! the number was {number}!")