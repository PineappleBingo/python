import pandas as pd
import numpy as np

location = pd.read_csv("data/CSV/location.csv")
votes = pd.read_csv("data/CSV/votes.csv")
# trim data
location = location.loc[:4]
votes = votes.drop(range(5,votes.shape[0]))

# sort data by columns
location = location.sort_values('state')
print(location)



# itertutples()
# print(location.head(5))
# for row in location.itertuples():
#     # getting row data with column index 2
#     print(row[2])

