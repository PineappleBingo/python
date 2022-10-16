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

# store chars in elems
for i in range(len(words)):
    chars.append(list(words[i]))

print(words)
print(chars)
wordsLen = len(words)
charsLen = len(chars)

# i : 0-5 : 6 elm
# j : 0-2 : 3 elm
for i in range(charsLen):
    for j in range(len(chars[0])):
        # print(chars[i][j])
        if chars[i][j] in words[i]:
            anags.append(words[i])
        # c, a, t

print(anags)