""" Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates. """


def remove_duplicates(list):
    return [ *set(list) ]

a = [ 1, 2, 3, 2, 4, 1, 5 ]

print(a)
print(remove_duplicates(a))