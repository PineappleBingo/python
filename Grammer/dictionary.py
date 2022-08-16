# classes
from pyexpat.errors import XML_ERROR_UNCLOSED_CDATA_SECTION, XML_ERROR_XML_DECL


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

print("-------------------------------------------------")

# function to return key for any value
def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key
    return "key doesn't exist"


def distance(x, y):
    # distance from 0, 0 = sqrt(x**2 + y**2)
    import math

    return math.sqrt(x ** 2 + y ** 2)


# pair of x, y coordinates
locations = [[1, 2], [-1, 3], [2, 3]]
NumStops = 2

# Opt1. Cast list to Tuple
X_dict = {tuple(locations[i]): None for i in range(len(locations))}
# {(1, 2): None, (-1, 3): None, (2, 0): None}

# Store Minimum Distance Delivery stops in List
X_stops = list()

for i in range(len(locations)):
    for j in range(len(locations[i])):
        # print(locations[i][j])
        dist = distance(locations[i][0], locations[i][1])
    X_dict[tuple(locations[i])] = dist

# {(1, 2): 2.23606797749979, (-1, 3): 3.1622776601683795, (2, 3): 3.605551275463989}

print(X_dict)
counter = 0
while counter < NumStops:
    # Find mininmum distance for each x, y cordinates
    minDist = X_dict[tuple(locations[0])]
    for key, value in X_dict.items():
        minDist = min(minDist, X_dict[key])

    stop = get_key(X_dict, minDist)
    X_stops.append(list(stop))
    locations.remove(list(stop))
    X_dict.pop(stop)
    counter += 1

print("Minimum Distance Delivery Stops:", X_stops)
