import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")

# read_sql_query
select_location = pd.read_sql_query("SELECT * FROM location;", engine)
print(select_location.head(5))

select_location1 = pd.read_sql_table("location", engine)
print(select_location1.head())

select_location2 = pd.read_sql_table("location", engine, index_col = "state")
print(select_location2.head())



# # select a specific column
# select_location1 = select_location["state"]
# print(select_location1.head(5))


