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

except cx_Oracle.Error as e:
    print(f"Error connecting to Oracle: {e}")
    exit()

try:
    sql = "SELECT * FROM SFE_DETAIL"
    index = "SSC_SEQ_NO"

    # Read SQL from oracleDB
    df_oracle = pd.read_sql(sql, con=connect, index_col=index)
    print(df_oracle.head(5))

    # Create CSV from SQL
    df_oracle.to_csv("D:\gitprojects\python\data\oracle_to_csv\oracle_to_csv.csv")

except KeyboardInterrupt:
    print("CLT-C:Terminate Server")
    pass

finally:
    print("----- DB disconnected -----")
    connect.close()
