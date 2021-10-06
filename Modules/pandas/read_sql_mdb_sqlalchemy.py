import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://root:little5@localhost:3306/k2")

# Querying
select_location = pd.read_sql_query("SLEECT * FROM location", engine)
print(select_location.head(5))