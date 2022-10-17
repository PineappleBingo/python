# classes
from email.policy import default
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

print("-------------------------------------------------")

words = ["cat", "tca", "atc", "pot", "opt", "pto"]

sortedWords = words[::]
# sort words and convert back to string
for i in range(len(words)):
    sortedWords[i] = ''.join(sorted(words[i]))

print(sortedWords)
# ['act', 'act', 'act', 'opt', 'opt', 'opt']

# Find indices of duplicate value method ------------ 1. using defulatdict
from collections import defaultdict

new_words = defaultdict(list)
for idx, data in enumerate(sortedWords):
    new_words[data].append(idx)

print(new_words)
new_words = dict(new_words)
print(new_words)
# {'act': [0, 1, 2], 'opt': [3, 4, 5]}

# -----------------------------------------------------
print("-----------------------------------------------")

# Find indices of duplicate value method ------------ 2
new_words2 = {sortedWords[i]: [] for i in range(len(sortedWords))}

# print(new_words2)
# {'act': [], 'opt': []}

sindx = 0
for i in range(len(sortedWords)):
    new_words2[sortedWords[i]].append(sortedWords.index(sortedWords[i], sindx))
    sindx += 1

print(new_words2)
# {'act': [0, 1, 2], 'opt': [3, 4, 5]}

# -----------------------------------------------------
print("-----------------------------------------------")


# conver set to list / remove uplicates
# nd_words = list(set(words))
# indices = []
# for idx, word in enumerate(words):
#     if word in nd_words:
#         indices.append(idx)
#         new_words[word] = indices

# print(new_words)


# indices = []
# new_words = {}
# def duplicates(elem):
#     if elem in words:
#         for idx, word in enumerate(words):
#             # print(idx, word)
#             if elem == word:
#                 indices.append(idx)
#                 new_words[word] = indices
#                 # print("word:", word, idx)
#     print(new_words)

# for word in words:
#     duplicates(word)


# # new_words = { word:[] for word, idx in enumerate(words) if word.count > 1  }
# new_words = {}
# indices = []
# for word, idx in enumerate(words):
#     if words.count(word) > 1:
#         new_words[word] = indices.append(idx)
# print(new_words)


# def findDuplicateIndex(iterable):
    


