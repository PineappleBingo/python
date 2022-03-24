
# when h < 0, h in [-0.1, -0.01]
h_list1 = np.arange(-0.1, 0, 0.01)
# when h > 0, h in [0.01, 0.1]
h_list2 = np.arange(0.01, 0.11, 0.01)
# concatenate
h_list3 = np.concatenate((h_list1, h_list2))

# For Three-point End Method
column1 = ["Three-Point End", "apprx. Error Bound", "Absolute Error", "Relative Error"]

# Assume that np.cos(x) returns exact value(s)
print("f(x) = sin(x) at x =", 1)
print("{:<17}{}".format("Exact Value:", np.cos(x)))
print("-------------------------------------------------")

rows1 = dict()
for h in h_list3:
    rows1[h] = [
                1,
                2,
                3,
                4
        ]