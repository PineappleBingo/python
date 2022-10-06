

num = [1, 2, 3, 4, 5]
N = len(num)

# For loop using in
for i in num:
    print("i:", i)

print("\n-------------------")

# For loop using range : 0 ~ 4
# 0 <= range() < 5
for i in range(N):
    print(num[i], end=" ")
    # 1 2 3 4 5

print("\n-------------------")

# For loop using rage : 1 ~ 4
# 1 <= range() < 4
for i in range(1, 4):
    print(num[i], end=" ")
    # 2 3 4

print("\n-------------------")

# For loop in reverse order 1
# 4 >= range() > -1 : 4 ~ 0 
for i in range(N-1, -1, -1):
    print(num[i], end=" ")
    # 5 4 3 2 1

print("\n-------------------")

# For loop in reverse order 2
for i in reversed(range(N)):
    print(num[i], end=" ")
    # 5 4 3 2 1

print("\n-------------------")

# For loop in reverse order 2
# 4 >= range() > 1: 4 ~ 1
for i in reversed(range(1, 4)):
    print(num[i], end=" ")
    # 4 3 2