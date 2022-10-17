# ---------------------------------------------------------
# input = ["cat", "tca", "atc", "pot", "opt", "pto"]
# output = [["cat", "tca", "atc"], ["pot", "opt", "pto"]]

# ---------------------------------------------------------
# a = ["a", "b", "c"]
# c = ["b", "a", "c"]
# print(a[0] in c)
# true
# ---------------------------------------------------------

# loop through input list elem.
# if c in elem[0] and elem[1] and elem[2] => store in list
# if c not in elems, removes

words = ["cat", "tca", "atc", "pot", "opt", "pto"]
chars = []
anags = []

# ---------------------------------------- wrong approach
# # store chars in elems
# for i in range(len(words)):
#     chars.append(list(words[i]))

# print(words)
# print(chars)
# wordsLen = len(words)
# charsLen = len(chars)

# # i : 0-5 : 6 elm
# # j : 0-2 : 3 elm
# for i in range(charsLen):
#     for j in range(len(chars[0])):
#         # print(chars[i][j])
#         if chars[i][j] in words[i]:
#             anags.append(words[i])
#         # c, a, t
# print(anags)
# ----------------------------------------

print(sorted(words[0]) == sorted(words[1]))
# true
print(sorted(words[0]) is sorted(words[1])) 
# false since each elem's memory location is different

# print(words)
# ['cat', 'tca', 'atc', 'pot', 'opt', 'pto']

sortedWords = []
# sort each elem and store to new list
for i in range(len(words)):
    # sortedWords.append(sorted(words[i]))
    words[i] = sorted(words[i])

print(words)
# [['a', 'c', 't'], ['a', 'c', 't'], ['a', 'c', 't'], ['o', 'p', 't'], ['o', 'p', 't'], ['o', 'p', 't']]

# print(sortedWords)
# [['a', 'c', 't'], ['a', 'c', 't'], ['a', 'c', 't'], ['o', 'p', 't'], ['o', 'p', 't'], ['o', 'p', 't']]

# sortedWordsSet = set(sortedWords)
# print(sortedWordsSet)

seen = set()
for j in range(len(words)):
    words[j] = ''.join(words[j])

# list to string conversion
print(words)
# ['act', 'act', 'act', 'opt', 'opt', 'opt']

index = []
output = []
idx = 0
for word in words:
    # index.append(words.index(word))
    
    if word in words:
        output.append(idx)
    idx+= 1
    # if word not in seen:
    #     seen.add(word)
print("output:", output)

for k, word in enumerate(words):
    if word in words:
        index.append(words.index(words[k]))

print("index:", index)


# print("index:", index)
# index: [0, 0, 0, 3, 3, 3]


# index = []
# # get index from the list which has the matched one
# for j in range(len(words)):
#     # if sortedWords[j] == sortedWords[k]
#     if sortedWords.count(sortedWords[j]) > 1:
#         # print(sortedWords.count(sortedWords[j]))
#         index.append(sortedWords.index(sortedWords[j]))
#         # it's index

# print(index)

# a = [1,2,3,2,1,5,6,5,5,5]
# # removed dupliccates
# b = set(a)
# uniq = []
# seen = set()

# for x in a:
#     if x not in seen:
#         uniq.append(x)
#         seen.add(x)

# print("a:", a)
# print("b:", b)
# print("unniq:", uniq)
# print("seen:", seen)



# seen = set()
# dupes = []

# for x in a:
#     if x in seen:
#         dupes.append(x)
#     else:
#         seen.add(x)



