
# Read CSV file using read_csv function

import pandas as pd

location = pd.read_csv("data/CSV/location.csv")
votes = pd.read_csv("data/CSV/votes.csv")

# 0. 
# by default pandas display first and last 5 rows of data
print(location)
# display first 8 rows only
print(location.head(8))
# display last 10 rows only
print(location.tail(10))
# display datatype of each column
print(location.dtypes)

# display technical summary of a dataframe
print(location.info())

# display quick overview of numerical data
print(location.describe())

# display maximum total_votes out of states
print(votes["total_votes"].max())
print(votes["republicans_2016"].max())

# 1.
# Select specific colum and display
total_votes = votes["total_votes"]
print(total_votes)

# display the number of rows and columns 
print(total_votes.shape)

# Select multiple columns and display
# To select multiple columns, use a list of column names within the selection brackets [].
locationInfo = location[["state", "county"]]
print(locationInfo)
print(locationInfo.shape)

# 2. How do I filter specific rows from DataFrame?

# dispaly states where over 50% of republican get votes
over50_republican = votes[votes["republicans_2016"] > 50]
print(over50_republican)

# display republican winning states
republicans = votes["republicans_2016"]
democrats = votes["democrats_2016"]

winningParty = votes[republicans > democrats]
# or winningParty = votes[( votes["republicans_2016"] ) > (votes["democrats_2016"]) ]
print(winningParty.head())

# isin()
# Select New York states and display
newyork = location[location["state"].isin(["New York"])]
print(newyork.head())

East = ['New York', 'New Jeresy', 'Florida']
EastenState = location[location["state"].isin(East)]
print(EastenState.head(5))

# Select only state column as an index, selecting by East index 
EastenState1 = location["state"][location["state"].isin(East)]
print(EastenState1.head(5))

# 3. How do I select specific rows and columns from a DataFrame?

# loc
# Select rows where total votes are less than 2000, column location_id
new_result = votes.loc[votes["total_votes"] < 2000, "location_id"]
print(new_result.head())

# iloc
# select row 0 ~ 2 and column 0 ~ 1
new_region = location.iloc[0:3, 0:2]
print(new_region)

# select row and column to assign new data 
location.iloc[0:2, 2] = "Empty"
print(location.head())

# Setting multiple items using a mask
# Select state starts with 'w' and manipulate county to 'W COUNTY'
NewLocation = location.copy()
mask = NewLocation['state'].str.startswith('W')
NewLocation.loc[mask, 'county'] = 'W COUNTY'
print(NewLocation.head(5))

# 4. Append a new column
