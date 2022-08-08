cdxes = ["a", "b", "C", "adc"]

# Generate a new dictionary & initialized with empty list
new_pfdx = { cdxes[i]: [] for i in range(len(cdxes)) }
print(new_pfdx)

# Create Temp list out of orig. list
tempArray = [ cdxes[i] for i in range(2)]
print(tempArray)

print("-----------------------------------")

# pair of x, y coordinates
locations = [[1, 2], [-1, 3], [2, 3]]

# Opt1. Cast list to Tuple
X_dict = {tuple(locations[i]): [] for i in range(len(locations))}

# {(1, 2): [], (-1, 3): [], (2, 0): []}
