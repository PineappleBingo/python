cdxes = ["a", "b", "C", "adc"]

# Generate a new dictionary & initialized with empty list
new_pfdx = {cdxes[i]: [] for i in range(len(cdxes))}
print(new_pfdx)

# Create Temp list out of orig. list
tempArray = [cdxes[i] for i in range(2)]
print(tempArray)

print("-----------------------------------")

# pair of x, y coordinates
locations = [[1, 2], [-1, 3], [2, 3]]

# Opt1. Cast list to Tuple
X_dict = {tuple(locations[i]): [] for i in range(len(locations))}

# {(1, 2): [], (-1, 3): [], (2, 0): []}

print("-----------------------------------")

seq = {"a", "b", "c"}
lis1 = [1, 2, 3]

# Mutable
new_dict0 = dict.fromkeys(seq,lis1)
print(new_dict0)
lis1.append(0)
print(new_dict0)
print("----------------")

# Immutable
new_dict1 = {key: list(lis1) for key in seq}
print(new_dict1)
lis1.append(4)
print(new_dict1)

print("----------------")

# Mutable
new_dict2 = {key: lis1 for key in seq}
print(new_dict2)
lis1.append(5)
print(new_dict2)


# Syntax
# newlist = [expression for item in iterable if condition == True]

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = []

for x in fruits2:
  if "a" in x:
    newlist1.append(x)

print(newlist1)
# ----------------------------------------------------------------
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = [x for x in fruits2 if "a" in x]

print(newlist2)

# ----------------------------------------------------------------
newlist3 = [x if x != "banana" else "orange" for x in fruits2]
# "Return the item if it is not banana, if it is banana return orange".
print("newlist3:",newlist3)
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']

newlist4 = []
for x in fruits2:
    if x!="banana":
        newlist4.append(x)
    else:
        newlist4.append("orange")

print("newlist4:",newlist4)
