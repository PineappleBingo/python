import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")

# read_sql_query()
#
select_location = pd.read_sql_query("SELECT * FROM location;", engine)
print(select_location.head(5))

select_location1 = pd.read_sql_table("location", engine)
print(select_location1.head())

select_location2 = pd.read_sql_table("location", engine, index_col = "state")
print(select_location2.head())


# read_sql_table()
# 
# read 'location' table with specific columns, 'state' and 'county' 
select_location3 = pd.read_sql_table("location", engine, columns=["state", "county"])
print(select_location3.head())


# read_sql_query()
select_location4 = pd.read_sql_query("SELECT * FROM votes;", engine)
print(select_location4.head())

select_location6 = pd.read_sql_query("SELECT location_id, total_votes FROM votes WHERE location_id BETWEEN 3000 AND 3100;", engine)
print(select_location6)




# # select a specific column
# select_location1 = select_location["state"]
# print(select_location1.head(5))


