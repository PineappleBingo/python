import mariadb
import pandas as pd

# MariaDB credentials
_HST = '127.0.0.1'
_DBN = 'k2'
_USR = 'root'
_PWD = 'little5'

try:
    mysql_con = mariadb.connect(host = _HST, user = _USR, password = _PWD, database = _DBN)
    print("----- DB connected -----")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    exit()

csr = mysql_con.cursor()
mysql_con.autocommit = False
             
try:    
    df_mysql = pd.read_sql('SELECT * FROM location;', con = mysql_con)
    print(df_mysql.head())

except mariadb.Error as e:
    print(f"Error Selecting Rows from MariaDB: {e}")
    mysql_con.rollback()
    mysql_con.close()
    exit()
            
mysql_con.commit()
