# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

print("write something, I will tell you if it is palindrome or not")
usr_input = input()
response = "palindrome"
for index, letter in enumerate(usr_input):
    if letter!=usr_input[len(usr_input)-1-index]:
        response = "not palindrome"
print(f"What you've written is {response}")