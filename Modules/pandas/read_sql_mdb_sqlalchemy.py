import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")

# Querying
select_location = pd.read_sql_query("SELECT * FROM location;", engine)
print(select_location.head(5))

# select a specific column
select_location1 = select_location["state"]
print(select_location1.head(5))