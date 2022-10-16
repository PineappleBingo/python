# Tutple

# Functions can take a variable number of arguments. A parameter name that begins with
# * gathers arguments into a tuple. For example, printall takes any number of arguments
# and prints them:

def printall(*args):
    print(args)

# The gather parameter can have any name you like, but args is conventional. Here’s how
# the function works:

printall(1, 2.0, '3')
# (1, 2.0, '3')

s = 'ABC'
t = 'abc'
u = [1, 2, 3]

print(zip(s, u))
# The result is a zip object that knows how to iterate through the pairs. The most common
# use of zip is in a for loop

for pairs in zip(s, t):
    print(pairs)

# A zip object is a kind of iterator, which is any object that iterates through a sequence.
# Iterators are similar to lists in some ways, but unlike lists, you can’t use an index to select
# an element from an iterator.

tuple_list = list(zip(s,u))
print(tuple_list)
print("tuple_list[0]", tuple_list[0])
print("tuple_list[0]", tuple_list[0][1]) # not work

# You can use tuple assignment in a for loop to traverse a list of tuples:
for letter, number in tuple_list:
    print(number, letter)

# has_match takes two sequences, t1
# and t2, and returns True if there is an index i such that t1[i] == t2[i]:

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

print(has_match(s, t))

# If you need to traverse the elements of a sequence and their indices, you can use the built-in
# function enumerate:

for index, element in enumerate('abc'):
    print(index, element)

# Combining dict with zip yields a concise way to create a dictionary:
d = dict(zip('abc', range(3)))
print(d)

# It is common to use tuples as keys in dictionaries (primarily because you can’t use lists). 
# 
# For example, a telephone directory might map from last-name, first-name pairs to telephone
# numbers. Assuming that we have defined last, first and number, we could write:

# directory[last, first] = number

# # The expression in brackets is a tuple. We could use tuple assignment to traverse this dictionary.
# for last, first in directory:
#     print(first, last, directory[last,first])
