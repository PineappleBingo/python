a = [1,2,3,2,1,5,6,5,5,5]
# b removed dupliccates automatically
b = set(a)
uniq = []
seen = set()

for x in a:
    if x not in seen:
        uniq.append(x)
        seen.add(x)

print("a:", a)
print("b:", b)
print("unniq:", uniq)
print("seen:", seen)

print("----------------------------------")

# if elem is already exists in a set, elem will not add
seen.add(1)
print("seen:", seen)

print("----------------------------------")