# ---------------------------------------
# find duplicates and remove
# String: orange apple banana orange
# ---------------------------------------

inputString="orange, apple, banana, orange, orange"

new_inputString = inputString.replace(", ", " ")
inputList=new_inputString.split()
# ['orange', 'apple', 'banana', 'orange', 'orange']

# remove duplicate
for n in inputList:
    if inputList.count(n) > 1:
        inputList.remove(n)
    
print(inputList)
# # ['apple', 'banana', 'orange']

# ---------------------------------------
# string modification
# ---------------------------------------
a_str = 'spamsisdeliciouss'
b_str = 'sabcs'
# print(a_str.find('s'))
# # 0
# print(a_str.find('s',2))
# # 4
# print(a_str.find('s',a_str.find('s')+1))
# 4
# Looping
print(list(a_str))

indexes = []
strLen = len(a_str)
strlenb= len(b_str)
stack = []

print(b_str.find('s'))
print(b_str.find('s', 10))
# print(b_str.find('b', 1))
# # for i in range(b_str):
# # print(b_str.find('a', b_str.find('a')+0))
print(b_str.find('s', b_str.find('s')+1))

# for i in range(5, len(b_str)+1):
#     print(i, len(b_str))


indexes = []
for i in range(len(b_str)):
    loc = b_str.find(b_str[i]) # 's' 0  
    # First indexes
    if indexes.count(loc) > 1:
        pass
    else:
        indexes.append(loc)  
    # searching for next index
    for j in range(loc + 1, len(b_str) + 1): # 's' 1 ~ len(b_str) : 4
        print("j=loc+1:", j)
        # index = b_str.find(b_str[j], b_str.find(b_str[j]) + loc)
        index = b_str.find(b_str[i], j) # 's' 4
        if index != -1:
            indexes.append(index)
            loc = index
            
    print(b_str[i], loc)

print(indexes)

    # pindex = b_str.find(b_str[i], index + 1)




# for i in range(strLen):
#     index = a_str.find("s")
      
    
#     if index == -1:
#         pass
#     else:
#         stack.append(index)
#         current = stack.pop()
        

#         indexes.append(index)
#         index = a_str.find("s", index+1)
#         print("inx:", index)

# print(indexes)



# count duplicates
cout_a_str = { c:a_str.count(c) for c in a_str }
print("countDuple_a_str:", cout_a_str)

# Store Duplicates' indexes 
indexDuple_a_str = { a_str[i]:[] for i in range(len(a_str))}

# Generate new_key
new_key = list(indexDuple_a_str)
# print("new_key:", new_key)
# ['s', 'p', 'a', 'm', 'i', 'd', 'e', 'l', 'c', 'o', 'u']

# print(new_key[0], indexDuple_a_str[new_key[0]])
# s []


# for c in new_key:
#     for j in range(len(a_str)):
#         indexDuple_a_str[c].append(a_str.find(c, a_str.find(c)+1))
#         # print(c, j)

# print("indexDuple_a_str:", indexDuple_a_str)

# a_str.find(a_str[i])]
# for i in range(len(a_str)):
#     a_str.find(a_str[i],)