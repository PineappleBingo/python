import os
os.getcwd()

#print out current directory
print(os.getcwd())

# 3 ways to read from files

# phonebook = open("phonbook.txt", 'r")

# phonebook.read()
# 'Seo: 12345511\n Jinho: 242121512\n'
# phonebook.readlines()
# ['Seo: 12345511\n', 'Jinho: 242121512\n']

# phonebook.seek(0) # tracker to 0
# phonebook.tell()  # tell us where we are in the file

# dir(phonebook)
# print all the method associated with the object


# compound statement

with open ("testfile.txt", "r+") as f:
    data = f.read()
    f.seek(0)
    f.write("new lines" + data)



f = open("test1.txt", "w")
print("fist line", file = f)
print("fist line", file = f)
print("fist line", file = f, flush = True)
f.close()

print("newyork", end="\n\n\n\n")