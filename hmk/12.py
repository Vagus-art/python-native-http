""" Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
 and makes a new list of only the first and last elements of the given list.
 For practice, write this code inside a function. """

"""
@param
"""
def first_and_last(list):
    copied_list = list.copy()
    first_el = copied_list[0]
    copied_list.reverse()
    last_el = copied_list[0]
    return [first_el, last_el]

a = [5, 10, 15, 20, 25]

print(first_and_last(a))