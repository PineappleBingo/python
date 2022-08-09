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
