cdxes = ["a", "b", "C", "adc"]

# Generate a new dictionary & initialized with empty list
new_pfdx = { cdxes[i]: [] for i in range(len(cdxes)) }
print(new_pfdx)

# Create Temp list out of orig. list
tempArray = [ cdxes[i] for i in range(2)]
print(tempArray)
