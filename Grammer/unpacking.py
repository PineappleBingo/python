# Packing and Unpacking Arguments in Python
# * (for tuples)
# ** (for dictionaries)

# UnPacking
# Example of UnPacking 1 

# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)
 
# Driver Code
my_list = [1, 2, 3, 4]
 
# Unpacking list into four arguments
fun(*my_list)

print("---------------")

# Example of UnPacking 2
def multiply(a, b):
    return a * b

numbers = [3, 5]
print(multiply(*numbers))
# Output: 15

print("---------------")

# Example of UnPacking 3
numbers = [1, 2, 3]
new_numbers = [0, *numbers, 4]
print(new_numbers)
# Output: [0, 1, 2, 3, 4]

print("---------------")

# Example of UnPacking 4 (Dictionary)
test_obj = { 'foo': 'bar' }
print({ **test_obj, 'foo2': 'bar2' })
# Output: {'foo': 'bar', 'foo2': 'bar2'}

print("---------------")
# Example of UnPacking 5 (Dictionary)
def fun(a, b, c):
    print(a, b, c)
 
# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)
# 2 4 10

print("---------------")

# Packing 
# When we don’t know how many arguments need to be passed to a python function, we can use Packing to pack all arguments in a tuple. 

# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    return sum(args)
 
print(mySum(1, 2, 3, 4, 5)) # 15
print(mySum(10, 20)) # 30


print("---------------")

def fun1(a, b, c):
    print(a, b, c)
 
# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
 
    # Convert args tuple to a list so we can modify it
    args = list(args)
 
    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'
 
    # UNPACKING args and calling fun1()
    fun1(*args)
 
# Driver code
fun2('Hello', 'beautiful', 'world!')

print("---------------")

def fun(**kwargs):
 
    # kwargs is a dict
    print(type(kwargs))
 
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
 
# Driver code
fun(name="geeks", ID="101", language="Python")