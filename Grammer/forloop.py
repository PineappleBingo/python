

num = [1, 2, 3, 4, 5]
N = len(num)

# For loop using in
for i in num:
    print("i:", i)

print("-------------------")

# For loop using range : 0 ~ 4
# 0 <= range() < 5
for i in range(N):
    print("num[i]:", num[i])

print("-------------------")

# For loop using rage : 1 ~ 4
# 1 <= range() < 4
for i in range(1, 4):
    print("num[i]:", num[i])

print("-------------------")

# For loop in reverse order
for i in range(N, -1, -1):
    print("num[i]:", num[i])