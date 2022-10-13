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


# ---------------------------------------