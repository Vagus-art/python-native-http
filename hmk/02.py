# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
print("Insert a number")
number = input()
response = "even" if int(number)%2==0 else "odd"
print(f"The number is {response}")