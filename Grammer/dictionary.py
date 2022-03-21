# classes
cdxes = ["a", "b", "C", "adc"]

# features
pfdx = [
    [0],
    [1],
    [2],
    [3],
    [0, 1],
    [0, 2],
    [0, 3],
    [1, 2],
    [1, 3],
    [2, 3],
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3],
    [0, 1, 2, 3],
]

# Generate a new dictionary & initialized with empty list
new_pfdx = {cdxes[i]: [] for i in range(len(cdxes))}
print("new_pfdx:", new_pfdx)

# Generate new_index
new_key = list(new_pfdx)
print("new_key:", new_key)

# Assign each classes with corresponding 12 possible features
for i in range(len(cdxes)):
    for j in range(len(pfdx)):
        new_pfdx[str(new_key[i])].append(pfdx[j])

print("new_pfdx:", new_pfdx)
