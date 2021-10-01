# List

A = [ 1, 2, 3, 4, 5]
B = [ 6, 7 ]

print("before append A : ",A)
A.append(9)
print("after append A : ",A)
A.extend(B)
print("After extend B : ",A)
# List appended to A
A.append(B)
print("After append B : ",A)


phone = '347-804-8479'
delimeter = '-'
new_phone = phone.split(delimeter) # split return list
print(new_phone)
#print(type(new_phone))

joint = ' '
re_union = joint.join(new_phone)
print(re_union)
#347 804 8479

# An object with more than one reference has more than one name, so we say that the object
# is aliased.
a = 'banana'
b = 'banana'
print(a is b)

a1 = ['b','a']
b1 = ['b','a']
print(a1 is b1)

# the append method modifies a list, but the + operator creates a
# new list.
t1 = [1, 2]
t2 = t1.append(3)
print("t1:",t1)
print(type(t2))
print("t2:",t2) #none

t3 = [1, 2]
t4 = t3 + [3]
print("t3:",t3)
print(type(t4))
print("t4:",t4)

# The slice operator creates a new list and the assignment makes t refer to it, but that doesn’t
# affect the caller.

def tail(t):
    return t[1:]

rest = tail(t4)
print("t4:",t4)



#Dictionary

MyDictionary = dict()
MyDictionary[1] = 'csc470'
MyDictionary[2] = 'csc335'
MyDictionary['3'] = 'csc59866'

print(MyDictionary)

MyDictionary1 = { 1: 'csc470', 2: 'csc335', '3':'csc59866'}
print(MyDictionary1)
print("length of Mydictionary1:", len(MyDictionary1))

vals = MyDictionary1.values()
print(vals)
print(type(vals))
print(MyDictionary1[1])

for i in MyDictionary1:
    print(MyDictionary1[i])
