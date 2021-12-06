import pandas as pd
import json

data = pd.read_excel("data/demo/SupervisorSig.xlsx")

# Method 1.
# Jason
commtTuple = data.agg(tuple, axis=1).tolist()
commtList = list(commtTuple[0])

# tutple to list of list
commtJson = json.dumps(commtTuple)
# parse jason string to list
rws = json.loads(commtJson)

# loop through each row in list, print element in string
for rw in rws:
    print(str(rw)[1:-1])

print("---------------------------------------")
# Method 2
#
# print(read_comment.agg(tuple, axis=1).tolist())


# print("---------------------------------------")
# Method 3
#
# aceess each row
# for row in read_comment.itertuples(index=False, name=None):
# row = json.loads(str(row))
# print (row)
# print ("index[" + str(row.Index) + "] = " + str(row)[0:-1])

# test = read_comment.apply(tuple, axis=1).tolist()
# test1 = json.loads(str(test)[1:-1])
# print(test1)

# Method 4
#

# Method 5
#

# # Iterating over one column - `f` is some function that processes your data
# result = [f(x) for x in df['col']]
# # Iterating over two columns, use `zip`
# result = [f(x, y) for x, y in zip(df['col1'], df['col2'])]
# # Iterating over multiple columns - same data type
# result = [f(row[0], ..., row[n]) for row in df[['col1', ...,'coln']].to_numpy()]
# # Iterating over multiple columns - differing data type
# result = [f(row[0], ..., row[n]) for row in zip(df['col1'], ..., df['coln'])]


# reference :
# https://stackoverflow.com/questions/7837722/what-is-the-most-efficient-way-to-loop-through-dataframes-with-pandas
