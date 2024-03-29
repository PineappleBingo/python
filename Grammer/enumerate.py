
values = ["a", "b", "c"]


# ------------------------------------
index = 0
for value in values:
    print(index, value)
    index += 1
print("----------------------------")

# range() and len() will create index automatically
for index in range(len(values)):
    value = values[index]
    print(index, value)

print("----------------------------")

# Ues numerate() -------------------
for count, value in enumerate(values):
    print(count, value)

print("----------------------------")

# apply ----------------------------
users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    print(user)