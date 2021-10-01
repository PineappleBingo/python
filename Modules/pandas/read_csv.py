
# Read CSV file using read_csv function

import pandas as pd

location = pd.read_csv("data/CSV/location - location.csv")
votes = pd.read_csv("/data/CSV/votes - votes.csv")

# # by default pandas display first and last 5 rows of data
# print(location)
# # display first 8 rows only
# print(location.head(8))
# # display last 10 rows only
# print(location.tail(10))
# # display datatype of each column
# print(location.dtypes)

# # display technical summary of a dataframe
# print(location.info())



# # display maximum total_votes out of states
# print(votes.max()) 