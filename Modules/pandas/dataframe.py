import pandas as pd
import numpy as np

location = pd.read_csv("data/CSV/location.csv")
votes = pd.read_csv("data/CSV/votes.csv")

location = location.loc[:4]
votes = votes.drop(range(5,votes.shape[0]))
print(votes)

# df = pd.DataFrame([['NewYork', 'NewJeresy', 'Florida']] * 3, columns = list("abc"))
# print(df.head())

# # display label of columns in list
# print(df.columns)
# # dispaly specified column
# print(df.columns[0])



# itertutples()
# print(location.head(5))
# for row in location.itertuples():
#     # getting row data with column index 2
#     print(row[2])

