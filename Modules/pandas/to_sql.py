import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")


df = pd.DataFrame(np.random(20,3), columns = list("abc"))
print(df)