""" Write a program (using functions!)
that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string: 

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""

def yoda_reverser(str):
    listed_string = str.split()
    listed_string.reverse()
    reversed_string = ""
    for word in listed_string:
        reversed_string += f" {word}"
    return reversed_string

print("write something:")
print(yoda_reverser(input()))