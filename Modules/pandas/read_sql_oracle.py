import cx_Oracle
import pandas as pd

# Oracle credentials
_USR = "admin"
_PWD = "SGlittle5^^^"
_DSN = "high"

try:
    connect = cx_Oracle.connect(user=_USR, password=_PWD, dsn=_DSN, encoding="UTF-8")
    print("----- DB connected -----")
    cursor = connect.cursor()

    df_oracle = pd.read_sql("SELECT * FROM SFE_DETAIL", con=connect)
    print(df_oracle.head())

except cx_Oracle.Error as e:
    print(f"Error connecting to Oracle: {e}")
    exit()
finally:
    print("----- DB disconnected -----")
    connect.close()
