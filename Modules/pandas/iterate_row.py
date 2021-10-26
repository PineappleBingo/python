import pandas as pd
import json

data = pd.read_excel('data/demo/SupervisorSig.xlsx')

print(data.index)
# print(read_comment.agg(tuple, axis=1).tolist())

commtTuple = data.agg(tuple, axis=1).tolist()
commtList = list(commtTuple[0])
# print(commtList)
print("commtJson:")

# tutple to list of list
commtJson = json.dumps(commtTuple)
print(commtJson)
rws = json.loads(commtJson)
print("---")
print(rws)
# print(commtJson[0:-1])

# for row in commtJson:
#     print('row', str(row[0:-1]))

# for rw in rws:
#     csr.execute('insert into \"all_' + _TBL + '\" values(' + str(rw)[1:-1] + ');')


# # Iterating over one column - `f` is some function that processes your data
# result = [f(x) for x in df['col']]
# # Iterating over two columns, use `zip`
# result = [f(x, y) for x, y in zip(df['col1'], df['col2'])]
# # Iterating over multiple columns - same data type
# result = [f(row[0], ..., row[n]) for row in df[['col1', ...,'coln']].to_numpy()]
# # Iterating over multiple columns - differing data type
# result = [f(row[0], ..., row[n]) for row in zip(df['col1'], ..., df['coln'])]