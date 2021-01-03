# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("Select a number")

number = input()

parsed_number = int(number)

for num in range(1,parsed_number):
    if parsed_number%num==0: print(num)