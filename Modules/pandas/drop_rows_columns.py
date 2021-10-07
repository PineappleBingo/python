import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")

# read_sql_query
select_location = pd.read_sql_query("SELECT * FROM location;", engine)
print(select_location.head(5))

select_location1 = pd.read_sql_table("location", engine)
# update column names
select_location1.columns = ["ID", "STATE", "COUNTY", "LON", "LAT"]
print(select_location1.head())

# deleting single column
# axis = 1, column / axis = 0, row
trimmed = select_location1.drop(labels = "LON", axis = 1)
trimmed = trimmed.drop(columns="LAT")
print(trimmed.head(5))

# display the number of rows and columns
print(trimmed.shape)
print(trimmed.shape[0], trimmed.shape[1])

# check for even / odd
colunms_to_keep = [x for x in range(select_location.shape[1]) if x % 2 == 0]
colunms_to_drop = [y for y in range(select_location.shape[1]) if y % 2 != 0]

print("Even Columns:", colunms_to_keep)
print("Odd Columns:", colunms_to_drop)

# delete odd number columns
trimmed1 = select_location.drop(columns = select_location.columns[colunms_to_drop])
print(trimmed1.head(5))
# delete even number columns
trimmed2 = select_location.drop(columns = select_location.columns[colunms_to_keep])
print(trimmed2.head(5))

# select_location2 = pd.read_sql_table("location", engine, index_col = "state")
# print(select_location2.head())


