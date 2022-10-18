# ---------------------------------------------------------
# input = ["cat", "tca", "atc", "pot", "opt", "pto"]
# output = [["cat", "tca", "atc"], ["pot", "opt", "pto"]]

# ---------------------------------------------------------
# a = ["a", "b", "c"]
# c = ["b", "a", "c"]
# print(a[0] in c)
# true
# ---------------------------------------------------------

# ---------------------------------------- wrong approach
# chars = []
# anags = []
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
# -------------------------------------------------------

# -------------------------------------------------------
# Solution 1
# -------------------------------------------------------
from collections import defaultdict

words = ["cat", "tca", "atc", "pot", "opt", "pto"]

st_words = words[::]
# sort elem and convert list back to string
for i in range(len(st_words)):
    st_words[i] = ''.join(sorted(st_words[i]))

print(st_words)
# ['act', 'act', 'act', 'opt', 'opt', 'opt']

# find duplicat elem indices
dp_words = defaultdict(list)
for idx, val in enumerate(st_words):
    dp_words[val].append(idx)

# restore defaltdict to dict
dp_wordsIdx = dict(dp_words)
# print(dp_wordsIdx)
# {'act': [0, 1, 2], 'opt': [3, 4, 5]}

# get new key
new_key = list(dp_words)
# ['act', 'opt']
# print(len(dp_wordsIdx))
# 2
# print(len(dp_wordsIdx[new_key[0]]))
# 3
# print(dp_wordsIdx[new_key[0]])
# [0, 1, 2]
# print(words[dp_wordsIdx[new_key[0]][0]])
# cat

result = []
for i in range(len(dp_wordsIdx)):
    output = []
    lenDpIdx = len(dp_wordsIdx[new_key[i]])
    for j in range(lenDpIdx):
        output.append(words[dp_wordsIdx[new_key[i]][j]])
    result.append(output)

print("result:", result)
# [['cat', 'tca', 'atc'], ['pot', 'opt', 'pto']]

# -------------------------------------------------------

# print(sorted(words[0]) == sorted(words[1]))
# # true
# print(sorted(words[0]) is sorted(words[1])) 
# false since each elem's memory location is different


# key = list(set(st_words))
# idx = 0

# olist = []
# for i in range(len(key)):
#     # if key[i] in words:
#     olist.append([])
# print("olist:", olist)

# output = [ ]
# print(output)

# for i in range(len(words)):
#     loc = st_words.index(st_words[i], idx)
#     output.append(words[loc])
#     print(words[loc])
#     idx += 1

# print("output:", output)

# from collections import defaultdict
# dp_words = defaultdict(list)

# for idx, val in enumerate(st_words):
#     dp_words[val].append(idx)

# dp_wordsIdx = dict(dp_words)
# print(dp_wordsIdx)
# # {'act': [0, 1, 2], 'opt': [3, 4, 5]}

# new_key = list(dp_words)
# # ['act', 'opt']

# print(words)
# print(st_words)
# print(dp_words)

# # get_words = defaultdict(list)

# if 



# if words[i] == dp_wordsIdx[i]:
    

# for i in range(len(words)):
#     if dp_words[words[i]] in words:
#         print("hi")


# output = []
# for 



# print(sortedWords)
# [['a', 'c', 't'], ['a', 'c', 't'], ['a', 'c', 't'], ['o', 'p', 't'], ['o', 'p', 't'], ['o', 'p', 't']]

# sortedWordsSet = set(sortedWords)
# print(sortedWordsSet)

# seen = set()
# for j in range(len(words)):
#     words[j] = ''.join(words[j])

# # list to string conversion
# print(words)
# # ['act', 'act', 'act', 'opt', 'opt', 'opt']

# index = []
# output = []
# idx = 0
# for word in words:
#     # index.append(words.index(word))
    
#     if word in words:
#         output.append(idx)
#     idx+= 1
#     # if word not in seen:
#     #     seen.add(word)
# print("output:", output)

# for k, word in enumerate(words):
#     if word in words:
#         index.append(words.index(words[k]))

# print("index:", index)


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



