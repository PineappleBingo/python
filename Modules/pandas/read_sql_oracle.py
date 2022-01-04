import cx_Oracle
import pandas as pd
from datetime import datetime

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

    # Create excel from SQL
    # df_oracle.to_excel("D:\gitprojects\python\data\oracle_to_csv\oracle_to_excel.xlsx", engine='xlsxwriter')

    writer = pd.ExcelWriter(
        "pandas_datetime.xlsx",
        engine="xlsxwriter",
        datetime_format="mmm d yyyy hh:mm:ss",
        date_format="mmmm dd yyyy",
    )

    # Convert the dataframe to an XlsxWriter Excel object.
    df_oracle.to_excel(writer, sheet_name="Sheet1")

    writer.close()

except KeyboardInterrupt:
    print("CLT-C:Terminate Server")
    pass

finally:
    print("----- DB disconnected -----")
    connect.close()
