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

# print(a_str.find('s'))
# # 0
# print(a_str.find('s',2))
# # 4
# print(a_str.find('s',a_str.find('s')+1))
# 4

# count duplicates
cout_a_str = { c:a_str.count(c) for c in a_str }
print("countDuple_a_str:", cout_a_str)

# Store Duplicates' indexes 
indexDuple_a_str = { c:a_str.find(c) for c in a_str}
print("indexDuple_a_str:", indexDuple_a_str)


# for i in range(len(a_str)):
#     a_str.find(a_str[i],)