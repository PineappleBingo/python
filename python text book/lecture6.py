# """ """ for formatting print
print("""hihih
fdfdfdf""")

# ord() prints unicode
# chr() prints character
print("B unicode = ", ord('B'))
print("b unicode = ",ord('b'))
print("10 = ", chr(222))

#string[a:b] -- a is inclusive, b is exclusive 
a = 'hello world'
print(a[0:])
print(a[:-1])
print(a[:4])
print(a[2:-2])
print(a[-1]) # print last character
# reverse string
print(a[::-1])

# copy string
new_a = a[:]
print(new_a)
print(new_a*3)
print('a' < 'b') # true

# string modification
a_str = 'spamsisdeliciouss'
new_str = a_str[:1] + 'P' + a_str[2:]
print(new_str)

# find fuction
print(a_str.find('s'))
print(a_str.find('s',2))
print(a_str.find('s',a_str.find('s')+1))

# # Join
# b = 'pineapple'
# print(b.join(['I like ', 'bingo']))

# # exeample
# c = 'Greetings'

# for i in range(len(c)):
#     print(c[:len(c)-i])

# for i in range(len(c)):
#     if(len(c)-i == 2):
#         break
#     else:
#         print(c[:len(c)-i])
