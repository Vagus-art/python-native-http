# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
print("Insert your name")
name = input()
print("Insert yor age")
age_str = input()
age_int = int(age_str)
print(f"{name}, you will be {age_int+100} years old in 100 years")