# Chapter Excercise

horizon = "-"

# Exercise 10.1. Write a function called nested_sum that takes a list of lists of 
# integers and adds up
# the elements from all of the nested lists. For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21
t = [[1,2], [3], [4,5,6]]
#print(t[0])
#print(t[0][0])
#print(t[0][1])
#print("length of t:",len(t))
#print("length of nested list:", len(t[0]))

def nested_sum_1(t):
    sum = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            sum += t[i][j]
    return sum

print(t)
print("nested sum of list:", nested_sum_1(t))
print(horizon*30, end='\n\n')

# def nested_sum_2(t):
#     sum = 0
#     index = 0
#     count = len(t)
#     while (count != 0):
#         if(len(t[index]) > 1):
#             for i in range(len(t[index])):
#                 sum += t[index][i]
#             index += 1
#             count -= 1
#         elif(len(t[index]) == 1):
#             sum += t[index][0]
#             index += 1
#             count -= 1
#     return sum

# print("nested sum of list:", nested_sum_2(t))


# Exercise 10.2. Write a function called cumsum that takes a list of 
# numbers and returns the cumulative sum; that is, 
# a new list where the ith element is the sum of the first i + 1 elements 
# from the original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cumsum(t1):
    sum = 0
    temp = []
    for i in range(len(t1)):
        sum = sum + t1[i]
        temp.append(sum)

    return temp

print(t1)
print(cumsum(t1))
print(horizon*30, end='\n\n')

# Exercise 10.3. Write a function called middle that takes a list 
# and returns a new list that contains all but the first and last elements. 
# For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]

t3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def middle(t):
    begin = int((len(t)-1)/2)
    end = begin + 2
    # print("begin:",begin)
    # print("end:",end)
    temp = t[begin:end]
    return temp

print(t3)
print("middle list:", middle(t3))
print(horizon*30, end='\n\n')


# Exercise 10.4. Write a function called chop that takes a list, 
# modifies it by removing the first and
# last elements, and returns None. For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]

t4 = [1, 2, 3, 4]
def chop(t):
    del t[0]
    del t[-1]
    # t = t.pop[0]
    # t = t.pop[-1]
    # t = t.remove[t[0]]
    # t = t.remove[t[-1]]

print(t4)
print("chop list:", chop(t4))
print("modified:",t4)
print(horizon*30, end='\n\n')


# Exercise 10.5. Write a function called is_sorted that takes a list 
# as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. 
# For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False

# in_list = input("Please Enter List(ex:[1,2,2,3]: ")

# def is_sorted_1(in_list):
#     temp1 = in_list.replace('[', '')
#     temp2 = temp1.replace(']', '')
#     new_list = temp2.split(",")
#     print("Input List:",new_list)
#     sortList = new_list[:]
#     sortList.sort() # return none 
#     print("Sorted List:",sortList)
    
#     return print(new_list is sortList)
    
# is_sorted_1(in_list)

t5 = [1, 2, 2, 4]
t6 = ['b', 'a', 'd']

def is_sorted_2(t):
    print("Input List:",t)
    temp = t[:]
    temp.sort()
    print("Sorted List:",temp)
    if( t == temp):
        return print(True)
    else:
        return print(False)
    
is_sorted_2(t5)
is_sorted_2(t6)

print(horizon*30, end='\n\n')


# Exercise 10.6. 
# Two words are anagrams if you can rearrange the letters 
# from one to spell the other.
# Write a function called is_anagram that takes two strings 
# and returns True if they are anagrams.

# str1 = input("Please Enter String 1:")
# str2 = input("Please Enter String 2:")

def is_anagram(str1,str2):
    listStr1 = list(str1)
    listStr2 = list(str2)
    lenStr1 = len(listStr1)
    lenStr2 = len(listStr2)
    isFound = True
    print(listStr1)
    print(listStr2)
    for i in range(lenStr1):
        for j in range(lenStr2):
            if(listStr1[i] != listStr2[j]):
                isFound = False

    if ((lenStr1 != lenStr2) and (isFound != True)):
        return False
    else:
        return True
    
# print(is_anagram(str1, str2))

print(horizon*30, end='\n\n')


# Exercise 10.7. Write a function called has_duplicates 
# that takes a list and returns True if there
# is any element that appears more than once. It should not modify 
# the original list.
t7 = [1,2,3,4,5,1,2,4,5]

def has_duplicates(t):
    isDuplicated = False
    temp = t[:]
    print("Input List:", temp)
    for i in range(len(temp)):
        if(temp.count(temp[i]) > 1):
            isDuplicated = True
    return isDuplicated

print(has_duplicates(t7))

print(horizon*30, end='\n\n')


# Write a function called in_bisect that takes a sorted list 
# and a target value and returns True if
# the word is in the list and False if it’s not.
# You start in the middle and check to see whether the word you are
# looking for comes before the word in the middle of the list. 
# If so, you search the first half of the list
# the same way. Otherwise you search the second half

words = ['abc', 'def', 'ghi','jkl','mop','qrs','tuv', 'wxy','z']

def in_bisect(words, word):
    liWords = words[:]
    liWords.sort() # sort list, list is now in an alphabetical order
    lenWords = len(liWords)

    index = int(lenWords/2)
    print("index:", index)
    print("sorted list:",liWords)

    isFound = False
    def search_half_left(inList, bound):
        half_left = inList[:bound]
        print("Half_Left:  ", half_left)
        for word in half_left:
            if ( word == searchWord ):
                isFound = True
                return isFound

    def search_half_right(inList, bound):
        half_right = inList[bound:]
        print("Half_Right:  ", half_right)
        for word in half_right:
            if ( word == searchWord):
                isFound = True
                return isFound
    
    searchWord = word
    middleWord = liWords[index]
    if searchWord < middleWord:
        search_half_left(liWords, index)
    elif searchWord > middleWord:
        search_half_right(liWords, index)
    else:
        isFound = True
        return isFound
        # when searchWord == middleWord         

print(in_bisect(words, 'ghi'))


# print('abc' == 'abc')