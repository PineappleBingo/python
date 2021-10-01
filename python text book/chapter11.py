# dictionary
horizon = "-"


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)

def histogram_get(s):
    d = dict()
    for c in s:
        d[c] += 1
        d.get(c, 0)
    return d

g = histogram('brontosaurus')
print(g)

# print dictionary
def print_hist(h):
    # usinf built-in function sorted()
    for key in sorted(h):
        print(key, h[key])

print_hist(g)

# Here is a function that takes a value and returns the first key that maps to that value:
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

# global variable

been_called = False
def example2():
    global been_called
    been_called = True

# The global statement tells the interpreter something like, “In this function, when I say
# been_called, I mean the global variable; don’t create a local one.”



# Excercise 
# Exercise 11.1. Write a function that reads the words in words.txt 
# and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to
# check whether a string is in the dictionary.

def exe11_1():
    isFound = False
    wordsDic = dict()
    file = open('words.txt', 'r', encoding="utf8")
    readList = file.readlines()
    print("Read List:",readList)
    
    for word in readList:
        word = word.replace('\n','') # remove \n
        try: 
            wordsDic[word] = int(word)
        except:
            wordsDic[word] = word
            isFound = True
    
    file.close()
    print("Dictionary:",wordsDic)
    return isFound

print("\nString is in the Dictionary?",exe11_1())
print(horizon*30, end='\n\n')


# Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates 
# that takes a list as a parameter and returns True if there is any object that 
# appears more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.

t7 = [1,2,3,4,5,1,2,4,5]
t8 = [1,1,2,3,4,5,5]

def has_duplicates(t):
    isDuplicated = False
    temp = t[:]
    t_dic = dict()
    print("Input List:", temp)
    for key in temp:
        if (key not in t_dic.keys()):
            t_dic[key] = list()
            # t_dic: {1: [], 2: [], 3: [], 4: [], 5: []}
            t_dic[key].append(key)
            # print("I'm not here", key)
        else:
            t_dic[key].append(key)
            isDuplicated = True
            # print("I'm here")
   
    print("Dictionary:",t_dic)
    return isDuplicated
    # d = dict()
    # for c in temp:
    #     print(c)
    #     d[c] += 1
    #     d.get(c, 0)
    # return d
    # print(d)

print("\nList has duplicates?",has_duplicates(t8))
print(horizon*30, end='\n\n')

def has_duplicates_1(t):
    isDuplicated = False
    temp = t[:]
    t_dic = dict()
    print("Input List:", temp)
    for key in temp:
        t_dic[key] = 0
        t_dic[key] += 1
        t_dic.get(key, 0)
        # return 0 if key does not exist in t_dic
        if (t_dic[key] != 0):
            isDuplicated = True
            # print("Duplicants:", t_dic[key])
            return isDuplicated
        else:
            return isDuplicated
        
print("\nList has duplicates?",has_duplicates_1(t8))
print(horizon*30, end='\n\n')


# d10 = {'zhen': 0,'zhen': 1,'zhen': 2,'zhen': 3, \
# 'cse': 0,'cse': 1, 'marquard': 0,'marquard': 1,'marquard': 2, \
# 'v': 0,'v': 1,'v': 2, 'cwen': 0, 'cwen': 1}

def common_name(d):
    
    print(d)
    print(len(d))
    # for name in d10:

common_name(d10)