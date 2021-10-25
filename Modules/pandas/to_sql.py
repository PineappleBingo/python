import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")


df = pd.DataFrame(np.random(20,3), columns = list("abc"))
print(df)

df.to_sql('users', con=engine)
engine.execute("SELECT * FROM users").fetchall()
[(0, 'User 1'), (1, 'User 2'), (2, 'User 3')]